from flask import Flask, jsonify
from passkey import key
import openai
from flask import render_template

openai.api_key = key

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('webpage.html', )
  

@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=1, size="1024x1024") 
  print(response)
  return jsonify(response)


app.run(host='0.0.0.0', port=8080)