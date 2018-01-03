from flask import Flask, url_for, request, render_template
from app import app
import redis

#connect to redis datastore
r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
#alternate ways to connect
#r = redis.StrictRedis()
#r = redis.StrictRedis('localhost',6379,0)

@app.route('/')
def hello():
    
    createLink = "<a href='"+ url_for('create') + "'>Create a question</a>"
    return """<html>
                <head>
                <title>Hello World !</title>
                <body>
                """ + createLink + """
                </body>
               </html>"""
@app.route('/create',  methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        # send the form to the user
        return render_template('createQ.html')
    elif request.method == 'POST':
        title = request.form['title']
        question = request.form['question']
        answer = request.form['answer']
        #store in dB
        #key will be title:question or title:answer(CONVENTION), and value - actual question/answer
        # countries:question, music:question
        # countries:answer, music:answer

        r.set(title + ":question", question)
        r.set(title + ":answer", answer)
        return render_template('createdQ.html', question=question)
    else:
        return "<h2>Invalid request</h2>"

@app.route('/question/<title>', methods=['GET', 'POST'])    
def question1(title):
    if request.method == 'GET':
        #send the user the form
        
        #Read question from datastore        
        question = r.get(title+':question')
        return render_template('answerQ.html', question=question)
    elif request.method=='POST':
        #User has attempted an answer, check if it is correct
        submittedAnswer = request.form['answer']

        #Read answer from data store
        answer = r.get(title+':answer')
        if submittedAnswer == answer:
            return render_template('correct.html')
        else:
            return render_template('incorrect.html', submittedAnswer= submittedAnswer, answer = answer)

    else:
        return '<h2>Invalid request</h2>'

        