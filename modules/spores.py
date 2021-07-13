from copper.modules import *
import time

SporesModule = Module(
    name="Spores",
    version="1.0",
    author="Vladislav117",
    folder="SporesData",
    subFolders=["users"]
)


class SporesUser:
    def __init__(self, uid):
        self.uid = str(uid)
        self.spores = 0
        self.time = 0

    def file(self):
        return SporesModule.folder(f"users\\{self.uid}.json")

    def load(self):
        if not os.path.exists(self.file()):
            self.save()
        else:
            data = Files.Reader.json(self.file())
            self.spores = data['spores']
            self.time = data['time']
        return self

    def save(self):
        data = {
            'spores': self.spores,
            'time': self.time
        }
        Files.Writer.json(self.file(), data)
        return self

    def startSession(self):
        self.load()
        return self

    def endSession(self):
        self.save()
        return self


class SporesConfig:
    delay = 12 * 60 * 60  # 12 H
    spores = 1


class SporesManager:
    @classmethod
    def addSpores(cls, user: SporesUser, spores: int):
        user.spores += spores

    @classmethod
    def getSpores(cls, user: SporesUser):
        return user.spores

    @classmethod
    def useThanks(cls, user: SporesUser, target: SporesUser):
        user.time = time.time()
        target.spores += SporesConfig.spores

    @classmethod
    def isTimeOk(cls, user: SporesUser):
        return time.time() - user.time > SporesConfig.delay


class Spores:
    @classmethod
    def thanks(cls, ci):
        user = SporesUser(ci.uid).startSession()
        srcParts = ci.src.replace('  ', '').replace('   ', '').split(' ')
        if len(srcParts) != 2:
            return CommandOutput(f"{ci.mention}, ошибка в записи команды.")
        else:
            if not SporesManager.isTimeOk(user):
                return CommandOutput(f"{ci.mention}, вы пока не можете это использовать.")
            else:
                targetUID = srcParts[1].replace("<@", '').replace(">", '').replace("&", '').replace("!", '')
                if targetUID == str(ci.uid):
                    return CommandOutput(f"{ci.mention}, нельзя благодарить себя же.")
                else:
                    target = SporesUser(targetUID).startSession()
                    SporesManager.useThanks(user, target)
                    user.endSession()
                    target.endSession()

                    return CommandOutput(f"<@{targetUID}>, вас поблагодарил {ci.mention}. "
                                         f"(Вы получили {SporesConfig.spores} {C.Emoji.spore})", points=3)

    @classmethod
    def spores(cls, ci):
        user = SporesUser(ci.uid).startSession()
        return CommandOutput(f"{ci.mention}, у вас {user.spores} {C.Emoji.spore}.")


Commands.register("thx", "Вы можете поблагодарить человека (Раз в 12 часов).", Spores.thanks)
Commands.register("spores", "Узнать количество стручков.", Spores.spores)
