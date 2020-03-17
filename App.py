from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
 

@app.route('/get',methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    print("msg from user is : "+ userText)
    return str(english_bot.get_response(userText))

@app.route("/")
def home():
    #return "<h1>Welcome to vit</h1>"
    return render_template("index.html")    
 
 
if __name__ == "__main__":
    app.run()

    