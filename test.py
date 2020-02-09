from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

vit_bot = ChatBot(name='PyBot1', read_only=False,
            logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how old are you',
              'I am 3 months old',
              'Which University',
              'Pune University',
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
              'i\'m pybot. ask me a math question, please.']
list1_trainer = ListTrainer(vit_bot)
for item in (small_talk):
    list1_trainer.train(item)

print(vit_bot.get_response(input("Hey")))

'''i =  1
while(i<=3):
    #print("\n")
    print(vit_bot.get_response(input()))
    i += 1
'''
    
