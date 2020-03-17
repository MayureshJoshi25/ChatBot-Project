from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
 
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'i\'m fine',
              'how are you ?'
              'i\'m ok',
              'glad to hear that.',
              'how old are you',
              'I am 3 months old',
              'How is Vit college',
              'Vit is a great college',
              'how are you?',
              'fine, you?',
              'i\'m cool.',
              'What is the full form of V.I.C.T.O.R.',
              'The full form of V.I.C.T.O.R. is Virtual Information Chatbot Technology for Optimal Response',
              'who are you?',
              'I am V.I.C.T.O.R. , the greatest chatbot',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m V.I.C.T.O.R.',
              'when was vit found?',
              'Vit was found in 1980',
              'history of the college?',
              'Vit was found in March 1980',
              'information on college?',
              'Very good college']

entity_placements = [
                        'placements',
                         '''In the past 9 years, around 111 companies have visited Vit every year,
                            The average salary package for the past eleven years is rs 4.59 lakhs pr annum''',

                        'Address',
                        '''Vishwakarma Institute of Technology666, 
                        Upper Indiranagar, Bibwewadi,Pune, Maharashtra, INDIA - 411 037.'''

                    ]              

inst_talk = [
                'History of Vit',
                '''Vishwakarma Institute of Technology, Pune,
                   a highly commendable private institute, occupies a place of pride amongst the premier technical institutes of the western region of India.''',
                'Where is vit college located',
                '''Vishwakarma Institute of Technology666, 
                  Upper Indiranagar, Bibwewadi,Pune, Maharashtra, INDIA - 411 037.''',
                'Contact Details of vit',
                'Contact Info : +91-20-2428 3001',
                'Which courses are offered in Vit?',
                '''Courses offered in vit are: 
                  Undergrad BTech in chemical , computer , ENTC  , Industrial and Production,
                  Instrumentation , IT , mechanical. 
                  Postgrad courses : MCA and Mtech 
                  Phd Programs.''',
                'Fees for BTech courses',
                'The fee for BTech courses is around 1,80,000',
                'What are the placements rates in Vit',
                '''In the past 9 years, around 111 companies have visited Vit every year,
                  The average salary package for the past eleven years is rs 4.59 lakhs pr annum''',
                'I dont care',
                'Ok'   
                ]

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

    