import pickle
import discord

from Scripts.path import getPath

from Scripts.ext import extractValue


def h_delChannel(message):
    return discord.Embed(title="!채널삭제 명령어 사용법",
                              description=f"!채널삭제\n"
                                          f"!지피티 명령을 사용할 수 있는 채널을 삭제합니다.\n"
                                          f"Admin만 사용할 수 있습니다.",
                              color=0x00aaaa)

def cmd_delChannel(message):
    adminList = []

    with open(getPath() + "Scripts\\Utilities\\command_chatGPT\\admin.pickle", "rb") as data:
        adminList = list(pickle.load(data))

    if message.author.name not in adminList:
        return

    channelID = str(message.channel.id)

    registerdChannels = []
    channel = []
    with open(getPath() + "Scripts\\Utilities\\command_chatGPT\\registerdChannel.pickle", "rb") as data:
        registerdChannels = list(pickle.load(data))

    isDeleted = False
    for i in range(len(registerdChannels)):
        c = list(registerdChannels[i])
        if c[0] == channelID:
            isDeleted = True
            channel = registerdChannels[i]
            registerdChannels.pop(i)
            break

    with open(f"{getPath()}Scripts\\Utilities\\command_chatGPT\\registerdChannel.pickle", "wb") as data:
        pickle.dump(registerdChannels, data)

    if not isDeleted:
        return discord.Embed(title=f"등록되어있는 채널이 아닙니다.",
                             description=f"등록되어있는 채널이 아니므로 삭제할 수 없습니다.",
                             color=0x00aaaa)

    return discord.Embed(title=f"채널이 삭제되었습니다.",
                          description=f"channelID:{channel[0]}\n"
                                      f"serverID:{channel[1]}\n"
                                      f"usage:{channel[2]}\n"
                                      f"나중에 꼭 다시 추가해주세요!",
                          color=0x00aaaa)