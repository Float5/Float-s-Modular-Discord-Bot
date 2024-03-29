import discord
import random

from Scripts.ext import extractValue

def h_rollingDice(message):
    return discord.Embed(title="!굴리기 명령어 사용법",
                              description=f"!굴리기 (숫자)"
                                          f"1~(숫자)까지의 랜덤한 정수를 뽑습니다",
                              color=0x00aaaa)

def cmd_rollingDice(message):
    values = extractValue(message.content[5:], 1)
    num = int(values[0])

    rnum = random.randint(1, num)

    return discord.Embed(title=f"주사위 굴리기 결과는?",
                          description=f"{rnum}",
                          color=0x00aaaa)