import json
import shelve

import os
from datetime import date

import requests
from bottle import template, static_file, request, post, get, run
from lxml import html

home = os.path.dirname(__file__)
open_downloads_dir = os.path.join(home, 'downloads', 'open')
umls_downloads_dir = os.path.join(home, 'downloads', 'umls')

downloads = shelve.open(os.path.join(home, 'downloads.pkl'), writeback=True)

h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
     "User-Agent": "python"}


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
    return item, sizeof_fmt(os.path.getsize(path)), date.fromtimestamp(
        os.path.getmtime(path)).strftime('%d %B %Y')


@get('/verify-umls/<filename>')
def verify_umls(filename):
    return template('verify-umls', {filename: filename})


@post('/verify-umls/<filename>')
def serve_umls(filename):
    username = request.forms.get('umlsuser')
    password = request.forms.get('umlspw')
    params = {'username': username, 'password': password}
    r = requests.post('https://utslogin.nlm.nih.gov/cas/v1/tickets/', data=params, headers=h)
    try:
        json.loads(r.text)
    except ValueError:
        try:
            doc = html.fromstring(r.text)
            tgt = doc.xpath('//form/@action')[0]
            if tgt is not None:
                return static_file(filename, umls_downloads_dir, download=True)
        except:
            return template('reject-umls')
    return template('reject-umls')


@get('/open/<filename:path>')
def serve_open(filename):
    count = downloads.get(filename, 0)
    downloads[filename] = count + 1
    return static_file(filename, open_downloads_dir, download=True)


@get('/')
def downloads():
    data = {
        'open_data': open_data_downloads(),
        'umls': umls_downloads(),
        'system': system_downloads()
    }
    return template('downloads', data)


if __name__ == '__main__':
    run(host='localhost', port=8080)
