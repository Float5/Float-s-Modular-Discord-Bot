import discord
import pickle

from Utilities.command_imLeave.command_imLeave import imLeave
from Scripts.path import getPath
from Secret.Secret import DiscordBotToken
from pickleManager import setPickle, getPickle


def executeCommand(message, h_or_cmd, command):
    from Utilities.command_howToUse import h_howToUse, cmd_howToUse
    from Utilities.command_OPGGValorant import h_OPGGValorant, cmd_OPGGValorant
    from Utilities.command_imLeave.command_imLeave import h_imLeave, cmd_imLeave
    from Utilities.minigames.command_rollingDice import h_rollingDice, cmd_rollingDice
    from Utilities.command_chatGPT.command_chatGPT import h_chatGPT, cmd_chatGPT
    from Utilities.command_chatGPT.command_test import h_test, cmd_test
    from Utilities.command_chatGPT.command_addChannel import h_addChannel, cmd_addChannel
    from Utilities.command_chatGPT.command_delChannel import h_delChannel, cmd_delChannel
    from Utilities.command_chatGPT.command_chatGPT_image import h_chatGPT_image, cmd_chatGPT_image
    from Utilities.command_chatGPT.command_price import h_price, cmd_price

    return locals()[h_or_cmd + command](message)




cmds = {
    "사용법" : "howToUse",
    "감스택" : "imLeave",
    "발로전적" : "OPGGValorant",
    "굴리기" : "rollingDice",
    "지피티" : "chatGPT",
    "테스트" : "test",
    "채널추가" : "addChannel",
    "채널삭제" : "delChannel",
    "가격" : "price"
    #"지피티이미지" : "chatGPT_image"

}

imLeaveWord = {"감", "rka", "Rka", "rKa", "rkA", "RKa", "RkA", "rKA", "RKA"}

path = "C:\\Users\\Sung_Huan\\Desktop\\Discord Bot\\"

print("all modules import complete")

client = discord.Client(intents=discord.Intents.all())

#-----------------------------------------------

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))

#-----------------------------------------------

@client.event
async def on_message(message):
    #exception
    if message.author == client.user:
        return

    if message.content in imLeaveWord:
        imLeave()

    h_or_cmd = message.content[0]
    if h_or_cmd == "?":
        h_or_cmd = "h_"
    elif h_or_cmd == "!":
        h_or_cmd = "cmd_"
    else:
        return

    if str(message.content).find(" ") != -1:
        spaceIndex = str(message.content).index(" ")
        command_in_kr = message.content[1:spaceIndex]
    else:
        command_in_kr = message.content[1:]
    command = cmds.get(command_in_kr)
    if command == None:
        return

    await message.channel.send(embed=executeCommand(message, h_or_cmd, command))
    return




token = DiscordBotToken
print("starting discord client")
client.run(token)