from nltk.chat.util import Chat
q1 = r'(.*)your name(.*)'
a1 = ['my name is chatbot','I Am a chatbot']
q2 = r'kiya kuch ajj acha hoga'
a2 = ['haan','mujhe kiya pata','mein kyo batau']
qa_pair = [
    [q1,a1],
    [q2,a2]
]
cb = Chat(qa_pair)
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    text = 'Hi '
    global cb
    if request.args.get('q') !=None:
        que = request.args.get('q')
        text = cb.respond(que)
        if text == None:
            text = 'unkonwn'
    return render_template('index.html',resp=text) #template tag :>{{ }},{% %}
@app.route('/new')
def new():
    return "<html><h1>Awsome</h1></html>"

app.run(debug=True)