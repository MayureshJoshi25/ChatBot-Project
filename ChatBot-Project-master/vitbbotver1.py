from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True,
            logic_adapters=['chatterbot.logic.BestMatch'])

history_talk_1 = ['about the college?',
                  'Vit was found in 1980',
                  'history of the college?',
                  'Vit was found in March 1980',
                  'information on college?',
                  'Very good college'
                 ]            

list_trainer = ListTrainer(my_bot)
for item in (history_talk_1):
    list_trainer.train(item)

#print(my_bot.get_response(input("Hello,how can I help you?")))                     