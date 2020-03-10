#We need to import two classes for this purpose: ChatBot from chatterbot and ListTrainer from chatterbot.trainers:
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Our bot will be an instance of the class ChatBot:
#You can provide read_only=True if you want to disable the bot’s ability to learn after the training (i.e. from actual conversations).
#logic_adapters is the list of adapters used to train the bot.
my_bot = ChatBot(name='PyBot', read_only=False,
                 logic_adapters=['chatterbot.logic.BestMatch',
                                 'chatterbot.logic.MathematicalEvaluation'])

#We are specifying the list of responses in the below part.
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how old are you',
              'I am 3 months old',
              'About college',
              'Vit is a great college',
              'i\'m cool.',
              'how are you?',
              'fine, you?',
              'who are you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'I am the best chatbot',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.',
              'when was vit found?',
              'Vit was found in 1980',
              'history of the college?',
              'Vit was found in March 1980',
              'information on college?',
              'Very good college']

entity_placements = [
                        'placements',
                         '''In the past 9 years, around 111 companies have visited Vit every year,
                            The average salary package for the past eleven years is rs 4.59 lakhs pr annum'''

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

                

#We can create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings:
list_trainer = ListTrainer(my_bot)
for item in (small_talk,entity_placements,inst_talk):
    list_trainer.train(item)
trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train('chatterbot.corpus.english.greetings')    

#You have to use get_response method to input things. Things inside the method are customizable.  
print(my_bot.get_response(input("Hello,how can I help you?")))
for i in range(10):
   print(my_bot.get_response(input()))
   print(i)
#print(my_bot.get_response())
