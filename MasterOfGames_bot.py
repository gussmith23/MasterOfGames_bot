#Written by Zachary Ranes
#Written for Python 3.4

import telebot
import random 

bot = telebot.TeleBot("294917770:AAHY8k4oLdBN-3haU29_Tywp0xXbScWGjps")
bot.game_state = 0
bot.players = []

@bot.message_handler(commands=['new_game'])
def new_game_resistance(message):
	bot.reply_to(message, "Cool, To play resistance we need 5 or more poeple \nIf you want to play type /join\n Once enough poeple haved joined start the game with /start_game")
	bot.game_state = 1

@bot.message_handler(commands=['join'])
def join_game_resistance(message):
	if bot.game_state > 1:
		bot.reply_to(message, "There is a game already going \nYou can not join a game already started")
	if bot.game_state == 1 and message.from_user.id in bot.players:
		bot.reply_to(message, "You have already joined the game")	
	if bot.game_state == 1 and message.from_user.id not in bot.players:
		bot.reply_to(message, "You have joined the game of resistance")
		bot.players.append(message.from_user.id)
	else:
		bot.reply_to(message, "There is no game to join")

@bot.message_handler(commands=['start_game'])
def start_game_resistance(message):
	if bot.game_state == 1 and len(bot.players) >= 3:
		bot.reply_to(message, "Let the game begine")
		bot.game_state = 2
		bot.send_message(bot.players[0], "You are Resistance")
		bot.send_message(bot.players[1], "You are a Spy")
		bot.send_message(bot.players[2], "You are Resistance")	
	if bot.game_state == 1 and len(bot.players) < 3:
		bot.reply_to(message, "Not enough players have joined to start the game \nYou need 5 or more to play, there are "+str(len(bot.players))+" playing now")

bot.polling()
