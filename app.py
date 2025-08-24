"""
givemetocode github project
GNU
pyredirect
"""

from flask import Flask, redirect, abort
import os

app = Flask(__name__)

@app.route('/<random_id>')
def redirect_to_url(random_id):
    try:
        with open('path.txt', 'r') as file:
            lines = file.readlines()
            paths = {line.split('=')[0]: line.split('=')[1].strip() for line in lines}
    except FileNotFoundError:
        return "Path file not found", 404

    target_url = paths.get(random_id)
    if target_url:
        return redirect(f'http://{target_url}')
    else:
        return abort(404)

"""
@app.route('/')
def rootpath() :
	return """ #<h2>givemetocode #project<h2><br><a href="https://givemetocode.com/">givemetocode.net</a>"""

"""
if __name__ == '__main__':
    app.run(debug=True)
