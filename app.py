from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "First Web App here! Hellooo :-) "

@app.route("/next/")
def next():
    return "This is cool! What' next?"

if __name__== '__main__':
    app.run()