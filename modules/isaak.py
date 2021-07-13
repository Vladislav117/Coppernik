from copper.modules import *

IsaakModule = Module(
    name="Isaak's soul",
    version="1.0",
    author="Vladislav117",
    folder="IsaakSoul"
)


class Isaak:
    @classmethod
    def routers(cls, ci):
        return CommandOutput("#ЯМЫROUTERS", instructions=[
            CommandInstruction("addReaction", {"emoji": C.Emoji.router}),
            CommandInstruction("addReaction", {"emoji": C.Emoji.greenrouter}),
            CommandInstruction("addReaction", {"emoji": C.Emoji.yellowrouter}),
            CommandInstruction("addReaction", {"emoji": C.Emoji.purplerouter}),
            CommandInstruction("addReaction", {"emoji": C.Emoji.rainbowrouter}),
            CommandInstruction("addReaction", {"emoji": C.Emoji.fatrouter})
        ])

    @classmethod
    def president(cls, ci):
        return CommandOutput("<@&759766498062630932>\n```Состав: сыр, вода питьевая, масло сливочное, сухое обезжиренное молоко, творог, сливки сухие, эмульгаторы орто- и полифосфаты, загустители Е1422 и каррагинан, сыворотка молочная сухая, регулятор кислотности - лимонная кислота, ароматизатор натуральный, стабилизатор ксантановая камедь.```")


Commands.register("routers", "Вспомнить времена, когда был жив Routers.", Isaak.routers)
Commands.register("president", "Пингует президента и показывает состав сыра President.", Isaak.president)
