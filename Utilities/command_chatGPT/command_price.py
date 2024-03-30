import discord

from Scripts.ext import extractValue
from Scripts.pickleManager import getPickle, setPickle

def h_price(message):
    return discord.Embed(title="!가격 명령어 사용법",
                              description=f"!가격 (토큰 or 현금)",
                              color=0x00aaaa)

def cmd_price(message):
    values = extractValue(message.content[4:], 1)
    TokenorCash = str(values[0])

    Tokens = getPickle("Scripts\\Utilities\\command_chatGPT\\token.pickle")

    Token = 0
    for t in Tokens:
        if t[0] == message.channel.id:
            Token = t[1]

    Cash = round(Token*0.0027, 4)

    isToken = TokenorCash == "토큰"
    title = "토큰" if isToken else "현금"
    descript = str(Token) + "토큰" if isToken else str(Cash) + "원"

    return discord.Embed(title=f"가격({title})",
                          description=f"{descript}",
                          color=0x00aaaa)