import discord
import time

from Scripts.ext import extractValue
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def h_OPGGValorant(message):
    return discord.Embed(title="!발로전적 명령어 사용법",
                              description=f"!발로전적 (ID)#(태그)",
                              color=0x00aaaa)

def cmd_OPGGValorant(message):
    values = extractValue(message.content[6:], 1)
    id = str(values[0])

    modifiedId = id.replace("#", "-")
    modifiedId = modifiedId.replace(" ", "%20")
    link = f"https://valorant.op.gg/profile/{modifiedId}"

    return discord.Embed(title=f"{id}의 발로란트 전적",
                          description=f"{link}",
                          color=0x00aaaa)