
from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def first_name(name):
    # return f'Hi' + name
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<words>')
def number_words(num,words):
    return f'{num*words}'




if __name__ =='__main__':
    app.run(debug=True,port=8000)