from fractions import Fraction

from pyparsing import (Combine, Optional, Regex, Word, infixNotation, nums,
                       oneOf, opAssoc)


class Parser:
    def __init__(self):
        rational_number = Combine(Optional(oneOf("+ -")) + Regex(r'\d+\.\d*|\.\d+')).setParseAction(lambda t: Fraction(t[0]))
        integer = Combine(Optional(oneOf("+ -")) + Word(nums)).setParseAction(lambda t: int(t[0]))
        number = rational_number | integer
        plus = oneOf('+ -')
        mul = oneOf('* /')

        self.parser = infixNotation(number, [
            (mul, 2, opAssoc.LEFT),
            (plus, 2, opAssoc.LEFT),
        ])

    def execute(self, expression):
        return self.parser.parseString(expression)
