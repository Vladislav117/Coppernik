from gmlib import *
from copper.daf import *


class ConstReplaceable:
    def __init__(self, text: str):
        self._text = text

    def format(self, keys: dict):
        return String.replaceKeys(self._text, keys)


class C:
    class Repl:
        moduleLogFormat = ConstReplaceable("[{moduleName}]:")

    class Dirs:
        modulesDataFolder = "ModulesData"
        coppernikDataFolder = "CoppernikData"

        DAF.mkdir(modulesDataFolder)
        DAF.mkdir(coppernikDataFolder)
        DAF.mkdir(f"{coppernikDataFolder}\\coppers")

    class Emoji:
        router = "<:router:783589022114775062>"
        greenrouter = "<:greenrouter:825782180298620979>"
        yellowrouter = "<:yellowrouter:825783050792468520>"
        purplerouter = "<:purplerouter:825782275366977617>"
        rainbowrouter = "<:rainbowrouter:805445123588096071>"
        fatrouter = "<:fatrouter:844150173868490752>"

        tokens = "<:token:832672840536031303>"
        copper = "<:copper:859492978158862346>"
        spore = "<:spore:864144231827374090>"

    class Perms:
        absoluteAdmin = '513755953712070657'

        @classmethod
        def isAAdmin(cls, uid):
            return str(uid) == '513755953712070657'

    class Bot:
        token = os.environ.get("COPPERNIK_TOKEN")
        prefix = '.'
        status = '.help'
