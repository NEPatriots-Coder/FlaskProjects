from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! Welcome to my dummy flask app!'

@app.route('/hello')
def say_hello():
    return "Hi there!"
    
@app.route('/bye')
def say_bye():
    return "bye there!"

if __name__ == '__main__':
    app.run(debug=True)