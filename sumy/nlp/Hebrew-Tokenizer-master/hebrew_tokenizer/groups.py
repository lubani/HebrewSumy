from enum import Enum, auto
class Groups(Enum): # type enumerator
    WHITESPACE = auto()
    DATE = auto()
    HOUR = auto()
    NUMBER = auto()
    URL = auto()
    PUNCTUATION = auto()
    ENGLISH = auto()
    HEBREW = auto()
    OTHER = auto()

