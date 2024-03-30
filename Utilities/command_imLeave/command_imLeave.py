import discord
import pickle

from Scripts.ext import extractValue
from Scripts.path import getPath
from Scripts.pickleManager import getPickle, setPickle

def h_imLeave(message):
    return discord.Embed(title="!감스택 명령어 사용법",
                              description=f"!감스택",
                              color=0x00aaaa)

def cmd_imLeave(message):
    stack = int(getPickle("Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle"))

    return discord.Embed(title=f"현재 감스택",
                          description=f"{stack}스택",
                          color=0x00aaaa)

def imLeave():
    stack = int(getPickle("Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle"))

    stack += 1

    setPickle("Scripts\\Utilities\\command_imLeave\\imLeaveStack.pickle", stack)