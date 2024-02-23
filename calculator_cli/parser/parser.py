from fractions import Fraction

from pyparsing import (Combine, Optional, ParseException, Regex, Word,
                       infixNotation, nums, oneOf, opAssoc)


class Parser:
    VALID_OPERATORS = ['+', '-', '*', '/']
    INVALID_OPERATORS = ['>', '<', '>=', '<=', '==', '!=', '**', '//', '%', '&', '|', '^', '<<', '>>', 'and', 'or', 'not']

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
        try:
            return self.parser.parseString(expression, parseAll=True)
        except ParseException as pe:
            if any(op in expression for op in self.INVALID_OPERATORS):
                raise ValueError("Contains operator not allowed") from pe
            elif expression.strip()[-1] in self.VALID_OPERATORS:
                raise ValueError("Ends with operator") from pe
            else:
                raise ValueError(f"Other invalid expression: {expression}") from pe
