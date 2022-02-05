from flask import Flask, render_template, url_for, request, redirect
from flask import Blueprint

# 関数名(index)でBlueprintオブジェクトを生成
index_app = Blueprint('index', __name__)

# ルートページ
@index_app.route('/')
def index():
    return render_template('index.html')