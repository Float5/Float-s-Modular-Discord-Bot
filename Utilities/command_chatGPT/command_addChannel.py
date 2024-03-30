import pickle
import discord

from Scripts.path import getPath

from Scripts.ext import extractValue
from Scripts.pickleManager import getPickle, setPickle


def h_addChannel(message):
    return discord.Embed(title="!채널추가 명령어 사용법",
                              description=f"!채널추가 (사용용도)\n"
                                          f"!지피티 명령을 사용할 수 있는 채널을 추가합니다.\n"
                                          f"Admin만 사용할 수 있습니다.",
                              color=0x00aaaa)

def cmd_addChannel(message):
    adminList = list(getPickle("Scripts\\Utilities\\command_chatGPT\\admin.pickle"))

    if message.author.name not in adminList:
        return


    values = extractValue(message.content[6:], 1, True)
    usage = str(values[0])
    channelID = str(message.channel.id)
    serverID = str(message.guild.id)

    channel = [channelID, serverID, usage]

    registerdChannels = list(getPickle("Scripts\\Utilities\\command_chatGPT\\registerdChannel.pickle"))

    isChanged = False
    for i in range(len(registerdChannels)):
        c = list(registerdChannels[i])
        if c[0] == channel[0]:
            isChanged = True
            registerdChannels.pop(i)
            break

    registerdChannels.append(channel)

    setPickle("Scripts\\Utilities\\command_chatGPT\\registerdChannel.pickle", registerdChannels)

    if isChanged:
        return discord.Embed(title=f"채널이 이미 등록되어있습니다.",
                             description=f"channelID:{channelID}\n"
                                         f"serverID:{serverID}\n"
                                         f"usage(변경됨):{usage}",
                             color=0x00aaaa)

    return discord.Embed(title=f"채널이 추가되었습니다!",
                          description=f"channelID:{channelID}\n"
                                      f"serverID:{serverID}\n"
                                      f"usage:{usage}",
                          color=0x00aaaa)