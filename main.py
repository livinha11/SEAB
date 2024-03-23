from flask import Flask, render_template, request, redirect

app = Flask('app')


@app.route('/')
def hello():
  return render_template('main.html')

@app.route('/about')
def sobre_nos():
  return render_template('info.html')

@app.route('/baixar')
def install():
  return render_template('pages.html')


app.run(host='0.0.0.0', debug=True)
