# Simple Flask project for web course

## Lesson 1 - MPA using Jinja2

### Step 1 - Install virtual environment

You can check python versions installed on your pc and paths to them with

- `py -0p` on windows  
or
- `ls -ls /usr/bin/python*` on unix

or just check current version with `python --version` and if it's ok create virtual environment from this python version with command `python -m venv venv`.

After that you have to activate this environment using

- `venv\Scripts\activate` on windows  
or
- `source venv/bin/activate` on unix

Now we can install any necessary package using preinstalled python package manager PIP. And it will be saved to our venv.

For the first step we need only flask. So execute `pip install flask` and that's it.

### Step 3 - Flask Hello, World!
Create file app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
And launch flask app
```bash
flask run
```

Now go to [127.0.0.1:5000](http://127.0.0.1:5000).

## Step 3 - Let's create a little project using jinja2
Move to the lesson_1 folder and launch flask app

## Lesson 2 - ORM, swagger and SPA

For the second lesson we also need flask_smorest and flask_sqlalchemy packages.
Install these packages and run app in lesson_2 folder. Then open [127.0.0.1:5000/docs](http://127.0.0.1:5000/docs).

We connected our app to local db and generated documentation via swagger.
 
*Next step - to create frontend part for our app on React.*