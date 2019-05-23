#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import io
from pathlib import Path
from flask import Flask, jsonify, request, redirect, url_for, send_file
from graphviz import Source

App = Flask(__name__, static_folder=Path.cwd() / 'static', static_url_path='')


@App.route('/')
def index():
    return App.send_static_file('index.html')


@App.route('/render', methods=['GET', 'POST'])
def render():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        rendered = render_graph(data['dot'])
        return send_file(
            io.BytesIO(rendered),
            attachment_filename='graph.png',
            mimetype='image/png'
        )
    else:
        return redirect(url_for('index'))


@App.errorhandler(404)
def page_not_found(err):
    return jsonify(error='404 NOT FOUND'), 404


def render_graph(dot):
    G = Source(dot)
    return G.pipe(format='png')


def main():
    App.debug = True
    App.use_reloader = True
    App.run(host='0.0.0.0', port=5000, threaded=True)


if __name__ == '__main__':
    main()
