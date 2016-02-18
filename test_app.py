from bottle import run

from biomedicus_downloads import app

run(app, host='localhost', port=8080)
