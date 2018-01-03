# TriviaQnA
A simple webapp built on Python Flask and Redis database
The webapp asks the user to submit a question and it's answer.
One can also attempt answers to existing questions (/question/title)

It is built on a virtual environment (venv) which has all the dependencies required.
If not installed already, install virtual environment on your local machine usinng `pip install venv`

Next go to the direcory of the project and activate the virtual envrironment `. venv/bin/activate`
While you are in virtual environment, you can run the webapp.
The application file is app.py

Note that, to get the app working one must have [Redis](https://redis.io/download) installed on the local machine and should be running.

To **Run the Webapp:**
1. `export FLASK_APP=app.py`
2. `flask run` OR `python -m flask run`

By default app runs on http://localhost:5000

To attempt an answer to already submitted question, go to /question/title (replace title with actual title of question)
