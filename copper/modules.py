from gmlib import *
from copper.const import *
from copper.daf import *
from copper.commands import *

class Module:
    _isLogEnabled = True

    def __init__(self, name: str, version: str, author: str, folder: str, subFolders=[]):
        self._name = name
        self._version = version
        self._author = author

        self._folder = Path(C.Dirs.modulesDataFolder, folder)

        DAF.mkdir(self.folder())
        for subFolder in subFolders:
            DAF.mkdir(self.folder(subFolder))

    def name(self):
        return self._name

    def version(self):
        return self._version

    def author(self):
        return self._author

    def log(self, *values):
        if self.__class__._isLogEnabled:
            print(C.Repl.moduleLogFormat.format({"moduleName": self._name}), *values)

    def enableLog(self):
        self.__class__._isLogEnabled = True

    def disableLog(self):
        self.__class__._isLogEnabled = False

    def folder(self, subFolder=None):
        if subFolder is None:
            return self._folder.__str__()
        else:
            return Path(self._folder.__str__(), subFolder).__str__()
