from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "First Web App here! Hellooo :-) "

@app.route("/next/")
def next():
    import os

    # Get the current user's home directory
    home_dir = os.path.expanduser("~")

    # Define the file name and path within the user's home directory
    file_name = "example.txt"
    file_path = os.path.join(home_dir, file_name)

    # Write content to the file
    content = "This is an example file."
    with open(file_path, "w") as file:
        file.write(content)

    print("File stored at:", file_path)

    return "This is cool! What' next?"




if __name__== '__main__':
    app.run()