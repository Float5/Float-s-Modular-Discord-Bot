import discord
import pickle

from Scripts.ext import extractValue
from Scripts.path import getPath

def h_imLeave(message):
    return discord.Embed(title="!감스택 명령어 사용법",
                              description=f"!감스택",
                              color=0x00aaaa)

def cmd_imLeave(message):
    stack = 0
    with open(getPath() + "Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle", "rb") as data:
        stack = int(pickle.load(data))

    return discord.Embed(title=f"현재 감스택",
                          description=f"{stack}스택",
                          color=0x00aaaa)

def imLeave():
    stack = 0
    with open(getPath() + "Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle", "rb") as data:
        stack = int(pickle.load(data))

    stack += 1

    with open(getPath() + "Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle", "wb") as data:
        pickle.dump(stack, data)