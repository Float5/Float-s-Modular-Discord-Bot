import discord
from Scripts.ext import extractValue

def h_test(message):
    return discord.Embed(title="!테스트 명령어 사용법",
                              description=f"!테스트"
                                          f"메시지 데이터가 IDE 콘솔창에 출력됩니다",
                              color=0x00aaaa)

def cmd_test(message):
    print(message)

    return discord.Embed(title=f"테스트 결과",
                          description=f"{message.author.name}",
                          color=0x00aaaa)