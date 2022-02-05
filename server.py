# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect
from appRoute.index import index_app
from appRoute.caesar import caesar_app

app = Flask(__name__)

app.register_blueprint(index_app)
app.register_blueprint(caesar_app)

if __name__ == "__main__":
    app.debug = True  # デバッグモード有効化
    app.run(host="127.0.0.1", port=8080)
          