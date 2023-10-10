from flask import Flask, request, render_template, render_template_string
import flask_mobility

app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello from Flask!'
