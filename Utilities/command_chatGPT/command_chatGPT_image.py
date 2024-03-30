import discord
import openai
import pickle

from dotenv import load_dotenv

from Scripts.ext import extractValue
from Scripts.path import getPath
from Secret.Secret import OpenAI_API_key

lastResponse = ""

def h_chatGPT_image(message):
    return discord.Embed(title="!지피티이미지 명령어 사용법",
                              description=f"!지피티이미지 (내용)"
                                          f"지피티가 내용에 대해 이미지를 만들어줍니다",
                              color=0x00aaaa)

def cmd_chatGPT_image(message):
    values = extractValue(message.content[5:], 1, True)
    content = str(values[0])

    registerdChannels = []
    with open(f"{getPath()}Scripts\\Utilities\\command_chatGPT\\registerdChannel.pickle", "rb") as data:
        registerdChannels = list(pickle.load(data))

    registerd = False
    for i in range(len(registerdChannels)):
        c = list(registerdChannels[i])
        if c[0] == str(message.channel.id) and c[2] == "chatGPT":
            registerd = True

    if not registerd:
        return

    if len(content) > 100:
        return discord.Embed(title=f"오류!",
                             description=f"당신은 글자 수 제한인 100글자를 넘겼습니다\n"
                                         f"100글자 이하로 작성해주세요",
                             color=0x00aaaa)

    openai.api_key = OpenAI_API_key

    response = openai.images.generate(
        model="dall-e-3",
        prompt=content,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    print(f"chatGPT:{image_url}")

    return discord.Embed(title=f"이미지 다운로드",
                          description=f"{image_url}",
                          color=0x00aaaa)