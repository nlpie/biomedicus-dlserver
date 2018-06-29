import shelve
import xml.etree.ElementTree

import os
from datetime import date

import requests
from bottle import Bottle, template, static_file, request

home = os.path.dirname(__file__)
open_downloads_dir = os.path.join(home, 'downloads', 'open')
umls_downloads_dir = os.path.join(home, 'downloads', 'umls')

license_code = os.environ['NLMLICENSE']

app = Bottle()

downloads = shelve.open(os.path.join(home, 'downloads.txt'), writeback=True)


def system_downloads():
    return build_files_list(os.path.join(open_downloads_dir, 'system'))


def open_data_downloads():
    return build_files_list(os.path.join(open_downloads_dir, 'data'))


def umls_downloads():
    return build_files_list(umls_downloads_dir)


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def build_files_list(directory):
    return [file_dict(directory, item) for item in sorted(os.listdir(directory), reverse=True)]


def file_dict(directory, item):
    path = os.path.join(directory, item)
    return {
        'file': item,
        'byte_string': sizeof_fmt(os.path.getsize(path)),
        'ctime': date.fromtimestamp(os.path.getmtime(path)).strftime('%d %B %Y')
    }


@app.get('/verify-umls/<filename>')
def verify_umls(filename):
    return template('verify-umls', {filename: filename})


@app.post('/verify-umls/<filename>')
def serve_umls(filename):
    username = request.forms.get('umlsuser')
    password = request.forms.get('umlspw')
    params = {'licenseCode': license_code, 'user': username, 'password': password}
    r = requests.post('https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser', params=params)
    element = xml.etree.ElementTree.fromstring(r.text)
    result_text = element.text
    if "true" in result_text:
        return static_file(filename, umls_downloads_dir)
    else:
        return template('reject-umls')


@app.get('/open/<filename:path>')
def serve_open(filename):
    count = downloads.get(filename, 0)
    downloads[filename] = count + 1
    return static_file(filename, open_downloads_dir)


@app.get('/')
def downloads():
    return template('downloads',
                    {'open_data': open_data_downloads(), 'umls': umls_downloads(),
                     'system': system_downloads()})
