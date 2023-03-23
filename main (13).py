from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# create a chatbot instance
chatbot = ChatBot('MyBot')

# create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# train the chatbot on English corpus
trainer.train('chatterbot.corpus.english')

# start the chatbot
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    else:
        bot_response = chatbot.get_response(user_input)
        print('Bot:', bot_response)
