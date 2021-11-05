from copper.modules import *
from random import shuffle, choice

VotingModule = Module(
    name="Voting",
    version="1.0",
    author="Vladislav117",
    folder="Voting",
    subFolders=[]
)


class VotingConfig:
    activeEmojiPacksNames = [
        "colors", "food"
    ]
    emojiPacks = {
        "colors": list("⚪⚫🔴🔵🟤🟣🟢🟡🟠"),
        "food": list("🍎🍌🥨🧀🍕🍔🍩🍫🍗")
    }

    @classmethod
    def getEmojiPack(cls):
        return cls.emojiPacks[choice(cls.activeEmojiPacksNames)]


class Voting:
    @classmethod
    def createMultiVote(cls, ci):
        allText = ci.src.replace(C.Bot.prefix + ci.command, '')
        voteParts = allText.rsplit(" ", 1)
        if len(voteParts) < 2:
            return CommandOutput(f"{ci.mention}, ошибка в написании команды.")
        else:
            variants = voteParts[1].split(',')
            if not (1 < len(variants) < 10):
                return CommandOutput(f"{ci.mention}, нужно использовать от 2 до 9 вариантов.")
            else:
                emojiPack = VotingConfig.getEmojiPack()
                shuffle(emojiPack)
                text = f"{ci.mention} проводит опрос:\n{voteParts[0]}\n"
                instructions = list()
                for index in range(len(variants)):
                    text += f"{emojiPack[index]} - {variants[index]}\n"
                    instructions.append(CommandInstruction("addReaction", {"emoji": emojiPack[index]}))
                return CommandOutput(text, deleteMessage=True, instructions=instructions)

    @classmethod
    def createVote(cls, ci):
        allText = ci.src.replace(C.Bot.prefix + ci.command, '')
        text = f"{ci.mention} проводит опрос:\n{allText}\n"
        instructions = [CommandInstruction("addReaction", {"emoji": "👍"}),
                        CommandInstruction("addReaction", {"emoji": "👎"})]
        return CommandOutput(text, deleteMessage=True, instructions=instructions)

    @classmethod
    def createIdea(cls, ci):
        allText = ci.src.replace(C.Bot.prefix + ci.command, '')
        text = f"У {ci.mention} есть идея:\n\n{allText}\n\n(Создайте ветку для обсуждения, API пока не поддерживает работу с ветками)\n\n<@404602495365677057>"
        instructions = [CommandInstruction("addReaction", {"emoji": "👍"}),
                        CommandInstruction("addReaction", {"emoji": "👎"}),
                        CommandInstruction("sendToAnotherChannel", {"channelId": "906212467527516200"})]
        return CommandOutput(text, deleteMessage=False, instructions=instructions)

    @classmethod
    def addVote(cls, ci):
        instructions = [CommandInstruction("addReactionToUserMessage", {"emoji": "👍"}),
                        CommandInstruction("addReactionToUserMessage", {"emoji": "👎"})]
        return CommandOutput(None, deleteMessage=False, instructions=instructions)


Commands.register("mvote", "Позволяет сделать голосование (до 9 вариантов).", Voting.createMultiVote)
Commands.register("vote", "Позволяет сделать простое голосование (Только за/против).", Voting.createVote)
# Commands.register("modidea", "Создаёт идею для мода в канале <#906212467527516200>", Voting.createIdea)
Commands.register("v", "Создаёт на сообщении с командой реакции за и против.", Voting.addVote)
