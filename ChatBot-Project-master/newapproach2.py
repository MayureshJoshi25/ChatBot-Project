#We need to import two classes for this purpose: ChatBot from chatterbot and ListTrainer from chatterbot.trainers:
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Our bot will be an instance of the class ChatBot:
#You can provide read_only=True if you want to disable the bot’s ability to learn after the training (i.e. from actual conversations).
#logic_adapters is the list of adapters used to train the bot.
my_bot = ChatBot(name='PyBot', read_only=False,
                 logic_adapters=['chatterbot.logic.BestMatch'])

#We are specifying the list of responses in the below part.
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'hey',
              'hello',
              'hii',
              'how old are you',
              'I am 3 months old',
              'i\'m cool.',
              'how are you?',
              'fine, you?',
              'who are you?',
              'I am the best chatbot,victor',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m victor',
              
             ]  


entity_placement = [
                        
                        'placements',
                        '''In the past 9 years, around 111 companies have visited Vit every year,
                        The average salary package for the past eleven years is rs 4.59 lakhs pr annum'''

                   ]            

entity_address = [
                        
                        'Address',
                        '''Vishwakarma Institute of Technology666, 
                        Upper Indiranagar, Bibwewadi,Pune, Maharashtra, INDIA - 411 037.'''
                 ]
                      

entity_location =  [
                        
                        'location',
                        '''Vishwakarma Institute of Technology666, 
                        Upper Indiranagar, Bibwewadi,Pune, Maharashtra, INDIA - 411 037.'''
                   
                   ]  

entity_contact_details = [

                             'Contact details',
                             'Contact Info : +91-20-2428 3001' 
                         
                         ]                   
                        
entity_courses = [

                        'courses',
                        '''Courses offered in vit are: 
                        Undergrad BTech in chemical , computer , ENTC  , Industrial and Production,
                        Instrumentation , IT , mechanical. 
                        Postgrad courses : MCA and Mtech 
                        Phd Programs.'''
                 ]

entity_fees = [
                    'fees',
                    'The fee for BTech courses is around 1,80,000'

              ]

entity_history = [
                  
                    'history',
                    '''Vishwakarma Institute of Technology, Pune, a highly commendable private institute, occupies a place of pride amongst the premier technical institutes of the western region of India. 
                    Established in the year 1983, financed and run by the Bansilal Ramnath Agrawal Charitable Trust, Pune. 
                    It is affiliated to the University of Pune . Within three decades, the institute marched towards the pinnacle of glory through its remarkable achievements and laurels in the field of engineering education of high calibre.
                    According to Indian history, 'Vishwakarma' is a divine architect-engineer. It is believed that He fashioned this world with His rare engineering skills. 
                    The Trust adopted this name with a vision to develop engineers of high calibre, who could take up challenges of any type of engineering job and become successful in the chosen career.'''

                 ] 

entity_about_college =  [
                       
                            'about the college',
                            '''Vishwakarma Institute of Technology, Pune, a highly commendable private institute, occupies a place of pride amongst the premier technical institutes of the western region of India. 
                            Established in the year 1983, financed and run by the Bansilal Ramnath Agrawal Charitable Trust, Pune. 
                            It is affiliated to the University of Pune . Within three decades, the institute marched towards the pinnacle of glory through its remarkable achievements and laurels in the field of engineering education of high calibre.
                            According to Indian history, 'Vishwakarma' is a divine architect-engineer. It is believed that He fashioned this world with His rare engineering skills. 
                            The Trust adopted this name with a vision to develop engineers of high calibre, who could take up challenges of any type of engineering job and become successful in the chosen career.'''

                         
                        ]


                        
                       



#We can create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings:
list_trainer = ListTrainer(my_bot)
for item in (small_talk,entity_placement,entity_address,entity_location,
             entity_contact_details,entity_courses,entity_fees,entity_history,entity_about_college):
    list_trainer.train(item)
#trainer = ChatterBotCorpusTrainer(my_bot)
#trainer.train('chatterbot.corpus.english.greetings')    

#You have to use get_response method to input things. Things inside the method are customizable.  
print(my_bot.get_response(input("Hello,how can I help you?")))
for i in range(10):
   print(my_bot.get_response(input()))
   #print(i)
#print(my_bot.get_response())
