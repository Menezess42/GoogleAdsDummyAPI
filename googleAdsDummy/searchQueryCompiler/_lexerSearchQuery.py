import re
from enum import Enum
from typing import Any, List


class TokenType(Enum):
    SELECT = "SELECT"
    FROM = "FROM"
    WHERE = "WHERE"
    AND = "AND"
    BETWEEN = "BETWEEN"
    ORDER_BY = "ORDER_BY"
    ASC = "ASC"
    LIMIT = "LIMIT"

    DOT = "DOT"
    COMMA = "COMMA"
    IQUAL = "IQUAL"
    MORE = "MORE"
    LESS = "LESS"
    DASH = "DASH"
    APOSTROPHE = "APOSTROPHE"

    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"

    EOF = "EOF"

class token:
    def __init__(self, type: TokenType, value: Any, position: int):
        self.type = type
        self.value = value
        self.position = position

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

        self.keywords = {
                "SELECT": TokenType.SELECT,
                "FROM": TokenType.FROM,....#HERE .....
                }
