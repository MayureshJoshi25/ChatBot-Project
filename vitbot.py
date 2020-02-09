#We need to import two classes for this purpose: ChatBot from chatterbot and ListTrainer from chatterbot.trainers:
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Our bot will be an instance of the class ChatBot:
#You can provide read_only=True if you want to disable the bot’s ability to learn after the training (i.e. from actual conversations).
#logic_adapters is the list of adapters used to train the bot.
my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

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
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

#We can create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings:
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

#You have to use get_response method to input things. Things inside the method are customizable.  
print(my_bot.get_response(input("Hello,how can I help you?")))
#print(my_bot.get_response())
