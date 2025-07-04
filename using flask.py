from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my house'

@app.route('/backgate')
def backgate():
    return 'there a yellow and balck keke hanging around there'

app.run('0.0.0.0')