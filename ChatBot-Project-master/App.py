from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
vit_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter" , logic_adapters=['chatterbot.logic.BestMatch',
                                 'chatterbot.logic.MathematicalEvaluation'])
 
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
              'i\'m V.I.C.T.O.R.',]

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
                'The fee for BTech courses is around 1,80,000'
                'How is the campus of vit'
                'The campus of vit is small but has a canteen, a fruit canteen, and a New Poona Bakery.'
                'Which Events take place in vit?'
                '''There are two main events in vit: Vishwakarandak an Inter-Departmental event. 
                And M`elange; an event in which colleges all around maharashtra compete.
                Another Event in vit is Aatmabodh.'''
                'clubs of vit'
                '''The three musketeers of the clubs in vit are: The Robotics Forum, Veloce and IEEE.
                Other clubs include DSC, TedX, Poetry club.'''
            ]

list_trainer = ListTrainer(vit_bot)

for item in (small_talk,entity_placements,inst_talk):
    list_trainer.train(item)

trainer = ChatterBotCorpusTrainer(vit_bot)

trainer.train("chatterbot.corpus.english.greetings")



@app.route('/get',methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    print("msg from user is : "+ userText)
    return str(vit_bot.get_response(userText))

@app.route("/")
def home():
    #return "<h1>Welcome to vit</h1>"
    return render_template("index.html")    
 
 
if __name__ == "__main__":
    app.run()

    