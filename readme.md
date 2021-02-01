## Basic concept:
Through a URL, a website is made availble, on whith which I am able to track a projects progress, challenges and tasks in general.

This is accomplished with a ticket system:

    - I can create a "Project container"

    - I Can create tickets and assign them to a project

    - Tickets can be visually marked by importance

    - I can move tickets between dedicated "purpose" or "Stage" areas, as in: "in progress, waiting for review, etc."
        - Theses stage titles can be customized.

    - I can do do various things like:
        - sorting
        - filtering
        - editing

This application will be build with:
Python 3.8.0
Python as backend base using flask

Flask         1.1.2
Flask micro framework

simplejson    3.17.2
SimpleJSON is a fast JSON implementation that is compatible with Python’s json module. It is preferred for JSON operations if it is installed.

python-dotenv 0.15.0
python-dotenv enables support for Environment Variables From dotenv when running flask commands.

watchdog      1.0.2
Watchdog provides a faster, more efficient reloader for the development server.

## Dev Setup:
Easy:
Get my "backlog-dev" venv and install it

If you are on Windows, the environment variable syntax depends on command line interpreter.

On Command Prompt:

pip install -r requirements.txt

FLASK_APP=app.py
set FLASK_ENV=development

And on PowerShell:
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

Then run the application using the development server:
flask run

Alternatively you can use python -m flask:
python -m flask run

{%  %}
