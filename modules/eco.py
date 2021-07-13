from copper.modules import *

EcoModule = Module(
    name="Economy",
    version="1.0",
    author="Vladislav117",
    folder="EcoData",
    subFolders=("users", "bank", "permissions")
)


class EcoUser:
    def __init__(self, uid):
        self.uid = str(uid)
        self.counters = {}

    def file(self):
        return EcoModule.folder(f"users\\{self.uid}.json")

    def startSession(self):
        self.load()
        return self

    def endSession(self):
        self.save()
        return self

    def load(self):
        if not os.path.exists(self.file()):
            self.save()
        else:
            self.counters = Files.Reader.json(self.file())
        return self

    def save(self):
        Files.Writer.json(self.file(), self.counters)
        return self


class EcoBank:
    counter = "routers"
    value = 4653750000

    @classmethod
    def file(cls):
        return EcoModule.folder("bank\\bank.json")

    @classmethod
    def load(cls):
        if not os.path.exists(cls.file()):
            cls.save()
        else:
            cls.value = Files.Reader.json(cls.file())

    @classmethod
    def save(cls):
        Files.Writer.json(cls.file(), cls.value)


EcoBank.load()


class EcoManager:
    @classmethod
    def initCounter(cls, user: EcoUser, counter: str):
        if counter not in user.counters:
            user.counters[counter] = 0

    @classmethod
    def getCounter(cls, user: EcoUser, counter: str):
        cls.initCounter(user, counter)
        return user.counters[counter]

    @classmethod
    def addCounter(cls, user: EcoUser, counter: str, value):
        cls.initCounter(user, counter)
        user.counters[counter] += value

    @classmethod
    def sendCounter(cls, user: EcoUser, counter: str, value, target: EcoUser):
        cls.initCounter(user, counter)
        cls.initCounter(target, counter)

        cls.addCounter(user, counter, -value)
        cls.addCounter(target, counter, value)

    @classmethod
    def sendToBank(cls, user: EcoUser, value):
        cls.initCounter(user, EcoBank.counter)

        cls.addCounter(user, EcoBank.counter, -value)
        EcoBank.value += value
        EcoBank.save()

    @classmethod
    def sendFromBank(cls, user: EcoUser, value):
        cls.initCounter(user, EcoBank.counter)

        cls.addCounter(user, EcoBank.counter, value)
        EcoBank.value -= value
        EcoBank.save()


class EcoPerms:
    bankEditors = ['513755953712070657']
    ecoEditors = []

    @classmethod
    def isBankEditor(cls, uid):
        return str(uid) in cls.bankEditors

    @classmethod
    def isEcoEditor(cls, uid):
        return str(uid) in cls.ecoEditors

    @classmethod
    def bankFile(cls):
        return EcoModule.folder("permissions\\bankEditors.json")

    @classmethod
    def ecoFile(cls):
        return EcoModule.folder("permissions\\bankEditors.json")

    @classmethod
    def addBankEditor(cls, uid):
        cls.bankEditors.append(str(uid))
        Files.Writer.json(cls.bankFile(), cls.bankEditors)

    @classmethod
    def addEcoEditor(cls, uid):
        cls.ecoEditors.append(str(uid))
        Files.Writer.json(cls.ecoFile(), cls.ecoEditors)

    @classmethod
    def removeBankEditor(cls, uid):
        if str(uid) in cls.bankEditors:
            cls.bankEditors.remove(str(uid))
            Files.Writer.json(cls.bankFile(), cls.bankEditors)

    @classmethod
    def removeEcoEditor(cls, uid):
        if str(uid) in cls.ecoEditors:
            cls.ecoEditors.remove(str(uid))
            Files.Writer.json(cls.ecoFile(), cls.ecoEditors)

    @classmethod
    def save(cls):
        Files.Writer.json(cls.bankFile(), cls.bankEditors)
        Files.Writer.json(cls.ecoFile(), cls.ecoEditors)

    @classmethod
    def load(cls):
        if not os.path.exists(cls.ecoFile()) or not os.path.exists(cls.bankFile()):
            cls.save()
        else:
            cls.bankEditors = Files.Reader.json(cls.bankFile())
            cls.ecoEditors = Files.Reader.json(cls.ecoFile())


EcoPerms.load()


class Eco:
    @classmethod
    def balance(cls, ci):
        user = EcoUser(ci.uid).startSession()
        return CommandOutput(f"{ci.mention}, у вас {EcoManager.getCounter(user, 'routers')} {C.Emoji.greenrouter}.")

    @classmethod
    def tokens(cls, ci):
        user = EcoUser(ci.uid).startSession()
        return CommandOutput(f"{ci.mention}, у вас {EcoManager.getCounter(user, 'tokens')} {C.Emoji.tokens}.")

    @classmethod
    def coins(cls, ci):
        user = EcoUser(ci.uid).startSession()
        return CommandOutput(f"{ci.mention}, у вас {EcoManager.getCounter(user, 'coins')} {C.Emoji.yellowrouter}.")

    @classmethod
    def pay(cls, ci):
        counter = 'routers'
        counterEmoji = C.Emoji.greenrouter
        user = EcoUser(ci.uid).startSession()
        srcParts = ci.src.replace('  ', '').replace('   ', '').split(' ')
        if len(srcParts) != 3:
            return CommandOutput(f"{ci.mention}, ошибка в записи команды.")
        else:
            if not srcParts[2].isdecimal():
                return CommandOutput(f"{ci.mention}, сумма запиана неправильно или она меньше 0.")
            else:
                value = int(srcParts[2])
                if value <= 0:
                    return CommandOutput(f"{ci.mention}, сумма не может быть меньше или равна 0.")
                else:
                    userBalance = EcoManager.getCounter(user, counter)
                    if userBalance < value:
                        return CommandOutput(f"{ci.mention}, у вас недостаточно {counterEmoji}.")
                    else:
                        targetUID = srcParts[1].replace("<@", '').replace(">", '').replace("&", '').replace("!", '')
                        target = EcoUser(targetUID).startSession()
                        EcoManager.sendCounter(user, counter, value, target)
                        user.endSession()
                        target.endSession()

                        return CommandOutput(f"<@{targetUID}>, вы получили {value} {counterEmoji} от {ci.mention}.", points=1)

    @classmethod
    def bankBalance(cls, ci):
        return CommandOutput(f"{ci.mention}, сейчас в банке находится {EcoBank.value} {C.Emoji.greenrouter}.")

    @classmethod
    def payToBank(cls, ci):
        counter = EcoBank.counter
        counterEmoji = C.Emoji.greenrouter
        user = EcoUser(ci.uid).startSession()
        srcParts = ci.src.replace('  ', '').replace('   ', '').split(' ')
        if len(srcParts) != 2:
            return CommandOutput(f"{ci.mention}, ошибка в записи команды.")
        else:
            if not srcParts[1].isdecimal():
                return CommandOutput(f"{ci.mention}, сумма запиана неправильно или она меньше 0.")
            else:
                value = int(srcParts[1])
                if value <= 0:
                    return CommandOutput(f"{ci.mention}, сумма не может быть меньше или равна 0.")
                else:
                    userBalance = EcoManager.getCounter(user, counter)
                    if userBalance < value:
                        return CommandOutput(f"{ci.mention}, у вас недостаточно {counterEmoji}.")
                    else:
                        EcoManager.sendToBank(user, value)
                        user.endSession()

                        return CommandOutput(f"{ci.mention}, вы успешно перевели в банк {value} {counterEmoji}.", points=1)

    @classmethod
    def payFromBank(cls, ci):
        if not EcoPerms.isBankEditor(ci.uid):
            return CommandOutput(f"{ci.mention}, у вас нет прав на выполнение данной команды.")
        else:
            counterEmoji = C.Emoji.greenrouter
            user = EcoUser(ci.uid).startSession()
            srcParts = ci.src.replace('  ', '').replace('   ', '').split(' ')
            if len(srcParts) != 2:
                return CommandOutput(f"{ci.mention}, ошибка в записи команды.")
            else:
                if not srcParts[1].isdecimal():
                    return CommandOutput(f"{ci.mention}, сумма запиана неправильно или она меньше 0.")
                else:
                    value = int(srcParts[1])
                    if value <= 0:
                        return CommandOutput(f"{ci.mention}, сумма не может быть меньше или равна 0.")
                    else:
                        if EcoBank.value < value:
                            return CommandOutput(f"{ci.mention}, в банке недостаточно {counterEmoji}.")
                        else:
                            EcoManager.sendFromBank(user, value)
                            user.endSession()

                            return CommandOutput(f"{ci.mention}, вы получили из банка {value} {counterEmoji}.")


Commands.register("balance", "Показывает ваш баланс.", Eco.balance)
Commands.register("tokens", "Показывает сколько у вас жетонов.", Eco.tokens)
Commands.register("coins", "Показывает сколько у вас монет.", Eco.coins)
Commands.register("pay", "Позволяет переводить средства.", Eco.pay)
Commands.register("balancebank", "Показывает сколько средств хранится в банке.", Eco.bankBalance)
Commands.register("paybank", "Позволяет переводить средства в банк.", Eco.payToBank)
Commands.register("takebank", "Позволяет получить средства из банка.", Eco.payFromBank)
