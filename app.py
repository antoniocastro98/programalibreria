from flask import Flask, render_template, abort
from lxml import etree
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")