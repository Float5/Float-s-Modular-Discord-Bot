import discord
import openai
import pickle

from Scripts.ext import extractValue
from Scripts.path import getPath
from Secret.Secret import OpenAI_API_key

lastResponse = ""

def h_chatGPT(message):
    return discord.Embed(title="!지피티 명령어 사용법",
                              description=f"!지피티 (내용)"
                                          f"지피티가 내용에 대해 답변해 줍니다",
                              color=0x00aaaa)

def cmd_chatGPT(message):
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
                                         f"50글자 이하로 작성해주세요",
                             color=0x00aaaa)


    openai.api_key = OpenAI_API_key

    messages = []

    messages.append({"role" : "user", "content" : content})

    completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    chat_response = completion.choices[0].message.content
    print(f"chatGPT:{chat_response}")

    lastResponse = chat_response

    return discord.Embed(title=f"답변",
                          description=f"{chat_response}",
                          color=0x00aaaa)