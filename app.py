from flask import Flask
import os
app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv(os.path.join(os.getcwd(),"demo.env"))


@app.route("/")
def index():
    key = os.getenv("MY_KEY")
    sec = os.getenv("SECRET")
    #sec = os.getcwd()
    return "First Web App here! Hellooo :-) " + str(key) + str(sec)

@app.route("/like/")
def like():

    logme("like")

    return "Like recorded"

@app.route("/dislike/")
def dislike():
    
    logme("dislike")
    return "DisLike recorded"


def logme(message):
    # Get the current user's home directory
    home_dir = "/home/logs"

    # Define the file name and path within the user's home directory
    file_name = message +".txt"

    file_path = os.path.join(home_dir, file_name)
    if not os.path.exists(home_dir):
        os.makedirs(home_dir)


    # if not os.path.exists("logs"):
    #     os.mkdir("logs")

    # Write content to the file
    content = "This is a "+ message
    with open(file_path, "a") as file:
        file.write(content+ "\n")
    print("File stored at:", file_path)

if __name__== '__main__':
    app.run()