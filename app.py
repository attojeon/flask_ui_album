from flask import Flask, render_template, request, redirect
import requests

app = Flask("app")

@app.route('/', methods=['GET'])
def index():
  return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    print(f'>>> email: {email}, password: {password}')

    return render_template('logined.html', email=email, message='로그인성공')

app.debug = True
app.run(host='0.0.0.0', port=8080)