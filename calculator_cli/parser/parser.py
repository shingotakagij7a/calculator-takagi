from fractions import Fraction

from pyparsing import (Combine, Optional, ParseException, Regex, Word,
                       infixNotation, nums, oneOf, opAssoc)
from pyparsing.results import ParseResults


class Parser:
    VALID_OPERATORS = ['+', '-', '*', '/']
    INVALID_OPERATORS = ['>', '<', '>=', '<=', '==', '!=', '**', '//', '%', '&', '|', '^', '<<', '>>', 'and', 'or', 'not']
    INPUT_MAX_VALUE = 1_000_000_000
    INPUT_MIN_VALUE = -1_000_000_000

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
            parsed_expression = self.parser.parseString(expression, parseAll=True)
            self._check_input_value_range(parsed_expression)
            return parsed_expression
        except ParseException as pe:
            if any(op in expression for op in self.INVALID_OPERATORS):
                raise ValueError("Contains operator not allowed") from pe
            elif expression.strip()[-1] in self.VALID_OPERATORS:
                raise ValueError("Ends with operator") from pe
            else:
                raise ValueError(f"Other invalid expression: {expression}") from pe

    def _check_input_value_range(self, parsed_expression):
        for token in parsed_expression:
            if isinstance(token, (int, Fraction)):
                if token > self.INPUT_MAX_VALUE or token < self.INPUT_MIN_VALUE:
                    raise ValueError("Value out of allowed range")
            elif isinstance(token, ParseResults):
                self._check_input_value_range(token)
