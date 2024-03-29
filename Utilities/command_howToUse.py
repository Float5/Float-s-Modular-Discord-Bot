import discord

from Scripts.ext import extractValue

def h_howToUse(message):
    return discord.Embed(title="!사용법 명령어 사용법",
                              description=f"!사용법 (테스트 밸류)",
                              color=0x00aaaa)

def cmd_howToUse(message):
    values = extractValue(message.content[5:], 1)
    value = str(values[0])

    return discord.Embed(title="사용법",
                          description=f"(대충 사용법 나중에 추가할거임)\n"
                                      f"테스트 밸류 : {value}",
                          color=0x00aaaa)