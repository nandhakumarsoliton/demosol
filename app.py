from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
    return "First Web App here! Hellooo :-) "

@app.route("/like/")
def next():

    logme("like")

    return "Like recorded"

@app.route("/dislike/")
def next():
    
    logme("dislike")
    return "DisLike recorded"


def logme(message):
    # Get the current user's home directory
    home_dir = "/home/logs"

    # Define the file name and path within the user's home directory
    file_name = message +".txt"

    file_path = os.path.join(home_dir, file_name)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # Write content to the file
    content = "This is a "+ message
    with open(file_path, "w") as file:
        file.write(content+ "\n")
    print("File stored at:", file_path)

if __name__== '__main__':
    app.run()