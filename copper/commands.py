from copper.const import *


class CommandInstruction:
    def __init__(self, id: str, params: dict):
        self.id = id
        self.params = params


class CommandOutput:
    def __init__(self, text, points=0, deleteMessage=False, instructions=[]):
        self.text = text
        self.points = points
        self.deleteMessage = deleteMessage
        self.instructions = instructions


class CommandInput:
    def __init__(self, src, uid, mention, message, command):
        self.src = src
        self.uid = uid
        self.mention = mention
        self.message = message
        self.command = command


class Command:
    def __init__(self, command: str, helpText: str, exe):
        self.command = command
        self.helpText = helpText
        self.exe = exe

    def execute(self, ci):
        return self.exe(ci)


class Commands:
    all = {}
    help = ""

    @classmethod
    def execute(cls, command: str, ci: CommandInput):
        if command in cls.all:
            return cls.all[command].execute(ci)

    @classmethod
    def register(cls, command: str, helpText: str, exe):
        cls.all[command] = Command(command=command, helpText=helpText, exe=exe)

    @classmethod
    def reloadHelp(cls):
        cls.help = "Помощь по командам:\n"
        for command in cls.all:
            cls.help += f"`{C.Bot.prefix+command}` - {cls.all[command].helpText}\n"


def getCopper(ci):
    def file(uid):
        return f"CoppernikData\\coppers\\{uid}.json"

    copper = 0
    if os.path.exists(file(ci.uid)):
        copper = Files.Reader.json(file(ci.uid))
    return CommandOutput(f"{ci.mention}, у вас {copper} {C.Emoji.copper}.")


def addCopper(uid, count):
    def file(uid):
        return f"CoppernikData\\coppers\\{uid}.json"

    copper = 0
    if os.path.exists(file(uid)):
        copper = Files.Reader.json(file(uid))

    copper += count
    Files.Writer.json(file(uid), copper)


Commands.register("help", "Помощь по командам.", lambda ci: CommandOutput(Commands.help))
Commands.register("copper", "Показывает количество вашей меди.", getCopper)


def execute(message):
    src = str(message.content)
    command = src.split(' ')[0].replace(C.Bot.prefix, '', 1)
    if command in Commands.all:
        ci = CommandInput(
            src=src,
            uid=message.author.id,
            mention=message.author.mention,
            message=message,
            command=command
        )
        co = Commands.execute(command, ci)

        if co.points > 0:
            addCopper(message.author.id, co.points)

        return co
    else:
        return None
