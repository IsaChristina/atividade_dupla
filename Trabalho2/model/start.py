from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder = '../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listagem')
def listagem():
    return render_template('listagem.html')

app.run(debug=True)