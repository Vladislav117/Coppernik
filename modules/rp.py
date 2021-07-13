from copper.modules import *
from random import choice

RPModule = Module(
    name="Role play",
    version="1.0",
    author="Vladislav117",
    folder="RPData"
)


class RPManager:
    @classmethod
    def getTry(cls):
        return choice(["Успешно", "Неуспешно"])

    @classmethod
    def getLie(cls):
        return choice(["Ложь распознана", "Вам поверили"])


class RP:
    @classmethod
    def me(cls, ci):
        text = ci.src.replace(C.Bot.prefix + ci.command, '')
        return CommandOutput(f"* {ci.mention} {text} *", deleteMessage=True)

    @classmethod
    def try_(cls, ci):
        text = ci.src.replace(C.Bot.prefix + ci.command, '')
        return CommandOutput(f"* {ci.mention} {text} * `[{RPManager.getTry()}]`", deleteMessage=True)

    @classmethod
    def say(cls, ci):
        text = ci.src.replace(C.Bot.prefix + ci.command, '')
        return CommandOutput(f"{ci.mention} говорит: \"{text} \"", deleteMessage=True)

    @classmethod
    def sayLie(cls, ci):
        text = ci.src.replace(C.Bot.prefix + ci.command, '')
        return CommandOutput(f"{ci.mention} говорит: \"{text} \" `[{RPManager.getLie()}]`", deleteMessage=True)


Commands.register("m", "Показывает действие от вашего лица. (/me)", RP.me)
Commands.register("t", "Показывает действие от вашего лица с успехом выполнения. (/try)", RP.try_)
Commands.register("s", "Показывает речь от вашего лица.", RP.say)
Commands.register("l", "Показывает лживую речь от вашего лица с успехом выполнения.", RP.sayLie)
