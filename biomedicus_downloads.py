import xml.etree.ElementTree

import os
import requests
from bottle import Bottle, template, static_file, request

home = os.path.dirname(__file__)
open_downloads_dir = os.path.join(home, 'downloads/open')
umls_downloads_dir = os.path.join(home, 'downloads/umls')

license_code = os.environ['NLMLICENSE']

app = Bottle()


def system_downloads():
    return os.listdir(os.path.join(open_downloads_dir, 'system'))


def open_data_downloads():
    return os.listdir(os.path.join(open_downloads_dir, 'data'))


def umls_downloads():
    return os.listdir(umls_downloads_dir)


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
    return static_file(filename, open_downloads_dir)


@app.get('/')
def downloads():
    return template('downloads',
                    {'open_data': open_data_downloads(), 'umls': umls_downloads(), 'system': system_downloads()})
