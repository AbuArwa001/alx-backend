# 0x02. i18n - Internationalization with Flask
### Overview
This project focuses on internationalizing a Flask web application using Flask-Babel. The goal is to create a multilingual web application that supports multiple languages and localizes timestamps.

### Learning Objectives
Parametrize Flask templates to display different languages.
Infer the correct locale based on URL parameters, user settings, or request headers.
Localize timestamps.
### Requirements
All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
All files should end with a new line.
A README.md file at the root of the project folder is mandatory.
Code should use the pycodestyle style (version 2.5).
The first line of all files should be exactly #!/usr/bin/env python3.
All *.py files should be executable.
All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
All classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)').
All functions and methods should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)').
Documentation must be a real sentence explaining the purpose of the module, class, or method.
All functions and coroutines must be type-annotated.
Setup Instructions
* 0. Basic Flask App
Create a basic Flask app with a single / route and an index.html template.

Files: 0-app.py, templates/0-index.html

# 0-app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()
<!-- templates/0-index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Welcome to Holberton</title>
</head>
<body>
    <h1>Hello world</h1>
</body>
</html>