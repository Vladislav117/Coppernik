import json
import os


class FixedValue:
    """FixedValue is an alternative to constants
    """

    def __init__(self, value):
        """Initializing the FixedValue object.

        :param value:
        """
        self._value = value

    def get(self):
        """Function that returns the value of a constant.

        :return:
        """
        return self._value

    def s(self):
        """Function that returns a constant value converted to a string using str().

        :return str:
        """
        return str(self._value)

    def __str__(self):
        """Function that returns a constant value converted to a string using str().

        :return str:
        """
        return str(self._value)

    def i(self):
        """Function that returns a constant value converted to an integer value using int().

        :return int:
        """
        return int(self._value)

    def __int__(self):
        """Function that returns a constant value converted to an integer value using int().

        :return int:
        """
        return int(self._value)

    def f(self):
        """Function that returns a constant value converted to a float value using float().

        :return float:
        """
        return float(self._value)

    def __float__(self):
        """Function that returns a constant value converted to a float value using float().

        :return float:
        """
        return float(self._value)

    def b(self):
        """Function that returns a constant value converted to a boolean value using bool().

        :return bool:
        """
        return bool(self._value)

    def __bool__(self):
        """Function that returns a constant value converted to a boolean value using bool().

        :return bool:
        """
        return bool(self._value)

    def fixed(self):
        """A function that returns a new FixedValue object with the same value.

        :return FixedValue:
        """
        return FixedValue(self._value)


class Value(FixedValue):
    """The Value class is an alternative to variables.
    """

    def __init__(self, value):
        """Initializing the Value object.

        :param value:
        """
        FixedValue.__init__(self, value=value)

    def set(self, value):
        """A function to change the value of the Value object.

        :param value:
        """
        self._value = value
        return self


class FixedPoint:
    # TODO: add documentation
    class Constants:
        # TODO: add documentation
        X_NAMES = ["x", "X"]
        Y_NAMES = ["y", "Y"]
        Z_NAMES = ["z", "Z"]

    def __init__(self, x=0, y=0, z=0):
        """Initializing the FixedPoint object.

        :param int x:
        :param int y:
        :param int z:
        """
        self._x = x
        self._y = y
        self._z = z

    def x(self):
        """Returns the value along the x-axis.

        :return int:
        """
        return self._x

    def y(self):
        """Returns the value along the y-axis.

        :return int:
        """
        return self._y

    def z(self):
        """Returns the value along the z-axis.

        :return int:
        """
        return self._z

    def get(self, coord='x'):
        """Returns the value along the selected axis.

        The available axis names are in the FixedPoint.Constants class.

        :return int:
        """
        if coord in self.__class__.Constants.X_NAMES:
            return self._x
        elif coord in self.__class__.Constants.Y_NAMES:
            return self._y
        elif coord in self.__class__.Constants.Z_NAMES:
            return self._z
        else:
            raise ValueError(f'\"{str(coord)}\" is the wrong axis name.')

    def list(self):
        """Returns values along three axes as a list.

        :return list:
        """
        return [self._x, self._y, self._z]

    def tuple(self):
        """Returns values along three axes as a tuple.

        :return tuple:
        """
        return self._x, self._y, self._z

    def __str__(self):
        """Returns values along three axes in string format as "{x; y; z}"

        :return:
        """
        return '{' + str(self._x) + '; ' + str(self._y) + '; ' + str(self._z) + '}'

    def fixed(self):
        # TODO: add documentation
        return FixedPoint(x=self._x, y=self._y, z=self._z)

    @classmethod
    def default(cls):
        # TODO: add documentation
        return FixedPoint(x=0, y=0, z=0)


class Point(FixedPoint):
    def __init__(self, x=0, y=0, z=0):
        FixedPoint.__init__(self, x=x, y=y, z=z)

    def setX(self, x=0):
        self._x = x
        return self

    def setY(self, y=0):
        self._y = y
        return self

    def setZ(self, z=0):
        self._z = z
        return self

    def set(self, coord='x', value=0):
        if coord in self.__class__.Constants.X_NAMES:
            self._x = value
        elif coord in self.__class__.Constants.Y_NAMES:
            self._y = value
        elif coord in self.__class__.Constants.Z_NAMES:
            self._z = value
        else:
            raise ValueError(f'\"{str(coord)}\" is the wrong axis name.')
        return self

    def addX(self, x=0):
        self._x += x
        return self

    def addY(self, y=0):
        self._y += y
        return self

    def addZ(self, z=0):
        self._z += z
        return self

    def add(self, coord='x', value=0):
        if coord in self.__class__.Constants.X_NAMES:
            self._x += value
        elif coord in self.__class__.Constants.Y_NAMES:
            self._y += value
        elif coord in self.__class__.Constants.Z_NAMES:
            self._z += value
        else:
            raise ValueError(f'\"{str(coord)}\" is the wrong axis name.')
        return self

    def reset(self):
        self._x = 0
        self._y = 0
        self._z = 0
        return self

    @classmethod
    def default(cls):
        return Point(x=0, y=0, z=0)


class FixedSize:
    class Constants:
        W_NAMES = ['w', 'W', 'width', 'Width', 'WIDTH']
        H_NAMES = ['h', 'H', 'height', 'Height', 'HEIGHT']
        D_NAMES = ['d', 'D', 'depth', 'Depth', 'DEPTH']

    def __init__(self, w=1, h=1, d=1):
        self._w = w
        self._h = h
        self._d = d

    def w(self):
        return self._w

    def h(self):
        return self._h

    def d(self):
        return self._d

    def width(self):
        return self._w

    def height(self):
        return self._h

    def depth(self):
        return self._d

    def get(self, side='width'):
        if side in self.__class__.Constants.W_NAMES:
            return self._w
        elif side in self.__class__.Constants.H_NAMES:
            return self._h
        elif side in self.__class__.Constants.D_NAMES:
            return self._d
        else:
            raise ValueError(f'\"{str(side)}\" is a wrong side value.')

    def V(self):
        return self._w * self._h * self._d

    def list(self):
        return [self._w, self._h, self._d]

    def tuple(self):
        return self._w, self._h, self._d

    def __str__(self):
        return '{' + str(self._w) + '; ' + str(self._h) + '; ' + str(self._d) + '}'

    def fixed(self):
        return FixedSize(w=self._w, h=self._h, d=self._d)

    @classmethod
    def default(cls):
        return FixedSize(w=1, h=1, d=1)


class Size(FixedSize):
    def __init__(self, w=1, h=1, d=1):
        FixedSize.__init__(self, w=w, h=h, d=d)

    def setW(self, w=1):
        self._w = w
        return self

    def setH(self, h=1):
        self._h = h
        return self

    def setD(self, d=1):
        self._d = d
        return self

    def setWidth(self, w=1):
        self._w = w
        return self

    def setHeight(self, h=1):
        self._h = h
        return self

    def setDepth(self, d=1):
        self._d = d
        return self

    def set(self, side='width', value=1):
        if side in self.__class__.Constants.W_NAMES:
            self._w = value
        elif side in self.__class__.Constants.H_NAMES:
            self._h = value
        elif side in self.__class__.Constants.D_NAMES:
            self._d = value
        else:
            raise ValueError(f'\"{str(side)}\" is a wrong side value.')
        return self

    def reset(self):
        self._w = 0
        self._h = 0
        self._d = 0
        return self

    @classmethod
    def default(cls):
        return Size(w=1, h=1, d=1)


class Cube:
    def __init__(self, position=Point.default(), size=Size.default()):
        self._position = position
        self._size = size

    def position(self):
        return self._position

    def pos(self):
        return self._position

    def size(self):
        return self._size

    def V(self):
        return self._size.V()

    def inCube(self, point: Point):
        return (self._position.x() <= point.x() <= self._position.x() + self._size.w()) and \
               (self._position.y() <= point.y() <= self._position.y() + self._size.h()) and \
               (self._position.z() <= point.z() <= self._position.z() + self._size.d())


class Map:
    def __init__(self, size=FixedSize.default()):
        self._size = size.fixed()

        self._layers = list()
        self.clear()

    def size(self):
        return self._size

    def clear(self):
        self._layers.clear()
        for d in range(self._size.d()):
            self._layers.append(list())
            for h in range(self._size.h()):
                self._layers[-1].append(list())
                for w in range(self._size.w()):
                    self._layers[-1][-1].append(None)
        return self

    def fill(self, formula):
        self._layers.clear()
        for d in range(self._size.d()):
            self._layers.append(list())
            for h in range(self._size.h()):
                self._layers[-1].append(list())
                for w in range(self._size.w()):
                    self._layers[-1][-1].append(formula(Point(x=w, y=h, z=d)))
        return self

    def get(self, position: Point):
        return self._layers[position.z()][position.y()][position.x()]


class Files:
    class Reader:
        @classmethod
        def text(cls, path: str, encoding='utf-8'):
            fp = open(path, encoding=encoding)
            data = fp.read()
            fp.close()
            return data

        @classmethod
        def json(cls, path: str, encoding='utf-8'):
            fp = open(path, encoding=encoding)
            data = json.load(fp)
            fp.close()
            return data

    class Writer:
        @classmethod
        def text(cls, path: str, content, encoding='utf-8'):
            fp = open(path, 'w', encoding=encoding)
            fp.write(content)
            fp.close()

        @classmethod
        def json(cls, path: str, content, encoding='utf-8'):
            fp = open(path, 'w', encoding=encoding)
            json.dump(content, fp)
            fp.close()

    @classmethod
    def all(cls, folder: str):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                result.append(os.path.join(root, name))
        return result

    @classmethod
    def allByExtension(cls, folder: str, extension: str):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                if name.endswith(f'.{extension}'):
                    result.append(os.path.join(root, name))
        return result

    @classmethod
    def allByExtensions(cls, folder: str, extensions: tuple):
        folder = folder.replace('/', '\\')
        result = []
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                for extension in extensions:
                    if name.endswith(f'.{extension}'):
                        result.append(os.path.join(root, name))
                        break
        return result

    @classmethod
    def getName(cls, path: str):
        return path.replace('/', '\\').split('\\')[-1]

    @classmethod
    def getOnlyName(cls, path: str):
        return path.replace('/', '\\').split('\\')[-1][:path.replace('/', '\\').split('\\')[-1].rfind(".")]


class Integer:
    """Static class that makes it easier to work with 'int' objects.

    """
    pass


class Float:
    """Static class that makes it easier to work with 'float' objects.

    """
    pass


class Boolean:
    """Static class that makes it easier to work with 'bool' objects.

    """
    pass


class String:
    """Static class that makes it easier to work with 'str' objects.

    """

    @classmethod
    def replaceKeys(cls, string: str, keys: dict, keySplitter=('{', '}')):
        # TODO: add documentation
        for key in keys:
            string = string.replace(keySplitter[0] + str(key) + keySplitter[1], str(keys[key]))
        return string


class List:
    """Static class that makes it easier to work with 'list' objects.

    """

    @classmethod
    def get(cls, list: list, index, default):
        # TODO: add documentation
        if len(list) > index:
            return list[index]
        else:
            return default


class Dictionary:
    """Static class that makes it easier to work with 'dict' objects.

    """

    @classmethod
    def get(cls, dictionary: dict, key, default):
        # TODO: add documentation
        if key in dictionary:
            return dictionary[key]
        else:
            return default


class Sine:
    def __init__(self, leftBound=-1, rightBound=1, step=1, start=None):
        self._leftBound = leftBound
        self._rightBound = rightBound
        self._value = leftBound
        if start is not None:
            self._value = start
        self._step = step
        self._rotation = 1

    def update(self, multiplier=1):
        self._value += self._step * multiplier * self._rotation
        if self._leftBound >= self._value:
            self._rotation = 1
            self._value = self._leftBound
        elif self._value >= self._rightBound:
            self._rotation = -1
            self._value = self._rightBound
        return self

    def __str__(self):
        return str(self._value)

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)


class UIDManager:
    """A static class that makes it easy to issue unique ids.
    For better class performance, it is recommended to add the uid() function to objects that have UIDs to get the UID.

    """
    _uid = 0
    _uid_counter = 0

    @classmethod
    def giveUID(cls):
        """Generates and returns a new unique identifier.

        :return int:
        """
        cls._uid_counter += 1
        return cls._uid_counter

    @classmethod
    def uid(cls):
        """Returns the unique identifier of the UIDManager class (0 by default).

        :return int:
        """
        return cls._uid


class UIDObject:
    """Generic object Main object for UIDManager.
    """
    def __init__(self):
        """Initializing the UIDObject object.
        """
        self._uid = UIDManager.giveUID()

    def uid(self):
        """Returns the unique identifier of the the object.

        :return int:
        """
        return self._uid


class Path:
    """An object that simplifies the work with the file system.
    """

    def __init__(self, *values):
        """Initializing the Path object.

        :param any values:
        """
        self._parts = []
        for value in values:
            if isinstance(value, Path):
                self._parts += value.list()
            elif isinstance(value, (tuple, list)):
                for element in value:
                    self._parts += Path(element).list()
            elif isinstance(value, str):
                if value.find("/") != -1 or value.find("\\") != -1:
                    value = value.replace("/", "\\").split("\\")
                    for element in value:
                        self._parts += Path(element)._parts
                else:
                    self._parts.append(value)
            else:
                self._parts.append(str(value))

    def path(self):
        """Returns path in a string format.

        :return str:
        """
        return self.__str__()

    def isFile(self):
        """Indicates whether the path is a file. (Defined by the extension point).

        :return bool:
        """
        return self._parts[-1].find('.') != -1

    def isFolder(self):
        """Indicates whether the path is a folder. (Defined by the extension point).

        :return bool:
        """
        return self._parts[-1].find('.') == -1

    def exists(self):
        """Determines if such a path exists.

        :return bool:
        """
        return os.path.exists(self.__str__())

    def length(self):
        """Determines the length of the path.

        :return:
        """
        return len(self._parts)

    def add(self, *values):
        """Adds value(s) to the end of the path.

        :param any values:
        :return:
        """
        self._parts = Path(self, values).list()

    def list(self):
        """Returns a list of all parts of the path in a string format.

        :return list:
        """
        return self._parts

    def __str__(self):
        """Returns path in a string format.

        :return str:
        """
        totalPath = ''
        for part in self._parts:
            totalPath += part + '\\'
        totalPath = totalPath[:-1]
        return totalPath

    def __add__(self, other):
        """Adds value(s) to the end of the path.

        :param any other:
        :return Path:
        """
        return Path(self, other)
