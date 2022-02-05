from flask import Flask, render_template, url_for, request, redirect
from flask import Blueprint

# 関数名(index)でBlueprintオブジェクトを生成
caesar_app = Blueprint('caesar', __name__)

# ルートページ
@caesar_app.route('/caesar')
def caesar():
    return render_template('caesar-html/caesar.html')