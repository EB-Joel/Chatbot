from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ya Boi")



trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

while True:
	try:
		chatbot_input = chatbot.get_response(input('You: '))
		print('bot: ', chatbot_input)

	except(KeyboardInterrupt, EOFError, SystemExit):
		break