from flask import Flask, request
#from flask_mobility import Mobility

app = Flask(__name__)
#Mobility(app)


@app.route('/')
def index():
    return 'Hello from Flask!'


#app.run(host='0.0.0.0', port=81)
