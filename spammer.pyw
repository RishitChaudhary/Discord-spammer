import asyncio # Importing asyncio to help us control the async functions
import os # Importing the os module to be able to do stuff with os
from random import randint, choice # Imported randint() for random numbers, choice() for random words
from discord.ext import commands # Importing commands from the discord.py module to define commands
os.system(F"cd {os.path.dirname(__file__)}") # Changes your current working directory to the one with the file


#################################################################################################################################

token="Your token goes here" # Your token goes inside the quotes
admins = []   # The id of the owner of the bot/yours goes here, whoevers id is here will be able to control the bot, seperate with ,

#################################################################################################################################


client = commands.Bot(command_prefix="!",self_bot=True) # Defining our bot's prefix and permissions
client._skip_check = lambda x, y: False    # True for bot only being able to see it's own messages

# Put your words/sentences in the 'words.txt' to randomly choose from, Seperated by newlines
with open('sentences.txt', 'r') as txt: # Opens the words inside the 'words.txt'
    sentences = txt.readlines() # Reads the lines in the 'words.txt' and assigns them as a list in the variable 'word'


async def num_spammer(ctx): # A async function for number spammer which'll be called later
    while True: # A while loop to continuosly send messages
        number = randint(99999,999999999) # The 'randint' method randomly chooses a number between the two number parameters
        await ctx.send(number) # Sends the message
        await asyncio.sleep(0.8) # The interval of per message, Decreasing might increase the chancess of getting disabled by discord


async def word_spammer(ctx): # A async function for words spammer which'll be called later
    while True: # A while loop to continuosly send messages
        sentence = choice(sentences).rstrip() # The 'choice' method randomly chooses a element from the list we defined above
        await ctx.send(sentence) # Sends the message
        await asyncio.sleep(0.8) # The interval of per message, Decreasing might increase the chancess of getting disabled by discord

# The function below is called when you use the command in the chat
@client.command() # A decorator to be called before making a discord command
async def startw(ctx): # Here we defined another async function but it'll become command becuase of the decorator above
    if ctx.author.id in admins:    # Checks if the command author is in the admin list
        global spamw # Variables inside a function are only usable inside that certain function, using the 'global' keyword helps make a variable usable anywhere in the code
        spamw = asyncio.create_task(word_spammer(ctx)) # Called the spammer function and assigned it to the variable 'spam' so that we can control it later
        await ctx.send("Starting the spammer") # Will be printed in the terminal if the '!start" command is used
    else:
        print(F"{ctx.author.name} is not allowed to perform this action")

@client.command() # A decorator to be called before making a discord command
async def startn(ctx): # Here we defined another async function but it'll become command becuase of the decorator above
    if ctx.author.id in admins: # Checks if the command author is in the admin list
        global spamn # Variables inside a function are only usable inside that certain function, using the 'global' keyword helps make a variable usable anywhere in the code
        spamn = asyncio.create_task(num_spammer(ctx)) # Called the spammer function and assigned it to the variable 'spam' so that we can control it later
        await ctx.send("Starting the spammer") # Will be printed in the terminal if the '!start" command is used
    else:
        print(F"{ctx.author.name} is not allowed to perform this action")

@client.command() # Represents another command
async def stopw(ctx): # Similar function to the one above this command but for stopping the spammer
    if ctx.author.id in admins: # Checks if the command author is in the admin list
        spamw.cancel() # Using the 'cancel()' method of asyncio to terminate the function that was running
        await ctx.send("Stopping the spammer") # Will be printed in the terminal if the '!stop" command is used

@client.command() # Represents another command
async def stopn(ctx): # Similar function to the one above this command but for stopping the spammer
    if ctx.author.id in admins: # Checks if the command author is in the admin list
        spamn.cancel() # Using the 'cancel()' method of asyncio to terminate the function that was running
        await ctx.send("Stopping the spammer") # Will be printed in the terminal if the '!stop" command is used

@client.event # A decorator specifying stuff going on with bot
async def on_ready(): # This function will be called when the bot is online
    print(F"{client.user.name} is ready!")

client.run(token, reconnect=True)
# Reconnect=True tells the code to try to reconnect if the internet gets disconnected, it'll keep trying till the internet is connected again