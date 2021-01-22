import json
import os
import shelve
from datetime import date

import requests
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

home = os.path.dirname(__file__)
umls_downloads_dir = os.path.join(home, 'downloads', 'umls')
open_downloads_dir = os.path.join(home, 'downloads', 'open')

download_counts = shelve.open(os.path.join(home, 'downloads.pkl'), writeback=True)

UTS_HEADER = {"Content-type": "application/x-www-form-urlencoded",
              "Accept": "text/plain",
              "User-Agent": "python"}


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def file_info(directory, item):
    path = os.path.join(directory, item)
    size_str = sizeof_fmt(os.path.getsize(path))
    date_str = date.fromtimestamp(os.path.getmtime(path)).strftime('%d %B %Y')
    return size_str, date_str


@app.route('/umls-file-info/<filename>', methods=['GET'])
@cross_origin()
def umls_file_info(filename):
    filename = str(filename)
    size, date = file_info(umls_downloads_dir, filename)
    return json.dumps({'size': size, 'date': date})


@app.route('/verify-umls/<_>', methods=['GET'])
def verify_umls(_):
    return render_template('verify-umls.html')


@app.route('/verify-umls/<filename>', methods=['POST'])
def serve_umls(filename):
    filename = str(filename)
    apikey = request.form.get('apikey')
    params = {'apikey': apikey}
    r = requests.post('https://utslogin.nlm.nih.gov/cas/v1/api-key', data=params,
                      headers=UTS_HEADER)
    if r.status_code == 201:
        count = download_counts.get(filename, 0)
        download_counts[filename] = count + 1
        return send_from_directory(umls_downloads_dir, filename, as_attachment=True)
    return render_template('reject-umls.html')


@app.route('/open-file-info/<filename>')
@cross_origin()
def open_file_info(filename):
    filename = str(filename)
    size, date = file_info(open_downloads_dir, filename)
    return json.dumps({'size': size, 'date': date})


@app.route('/open/<filename>')
def serve_open(filename):
    filename = str(filename)
    count = download_counts.get(filename, 0)
    download_counts[filename] = count + 1
    return send_from_directory(open_downloads_dir, filename, as_attachment=True)
