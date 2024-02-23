from pyparsing import *


class Parser:
    def __init__(self):
        integer = Word(nums)
        plus = Literal('+')
        self.expr = integer + ZeroOrMore(plus + integer)

    def parse(self, text):
        return self.expr.parseString(text)
