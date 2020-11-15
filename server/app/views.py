# views.py

from flask import Flask, render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Wohnzimmer.html')
def Wohnzimmer():
    return render_template("Wohnzimmer.html")

@app.route('/Schlafzimmer.html')
def Schlafzimmer():
    return render_template("Schlafzimmer.html")

@app.route('/Flur_Eingang.html')
def Flur_Eingang():
    return render_template("Flur_Eingang.html")

@app.route('/Flur_Bad.html')
def Flur_Bad():
    return render_template("Flur_Bad.html")