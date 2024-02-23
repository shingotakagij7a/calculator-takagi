from pyparsing import (Combine, Optional, Word, infixNotation, nums, oneOf,
                       opAssoc)


class Parser:
    def __init__(self):
        integer = Combine(Optional(oneOf("+ -")) + Word(nums)).setParseAction(lambda t: int(t[0]))
        plus = oneOf('+ -')
        mul = oneOf('* /')

        self.parser = infixNotation(integer, [
            (mul, 2, opAssoc.LEFT),
            (plus, 2, opAssoc.LEFT),
        ])

    def execute(self, expression):
        return self.parser.parseString(expression)
