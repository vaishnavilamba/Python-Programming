from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the flask Course. This is Best Flask Course."

@app.route('/index')
def index():
    return "Welcome to the index screen."

if __name__=='__main__':
    app.run(debug=True)