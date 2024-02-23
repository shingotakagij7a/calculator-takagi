from fractions import Fraction

from calculator_cli.arithmetic_operator.operator import Operator
from calculator_cli.parser.parser import Parser


class Evaluator:
    SINGLE_OPERAND_LENGTH = 1
    FIRST_OPERAND_INDEX = 0
    OPERATOR_INDEX = 1
    SECOND_OPERAND_INDEX = 2
    OUTPUT_MAX_VALUE = 1_000_000_000
    OUTPUT_MIN_VALUE = -1_000_000_000

    def __init__(self):
        self.operator = Operator()
        self.parser = Parser()

    def execute(self, expression):
        parsed_expression = self.parser.execute(expression)
        result = self._evaluate_parsed_expression(parsed_expression)
        if result > self.OUTPUT_MAX_VALUE or result < self.OUTPUT_MIN_VALUE:
            raise ValueError("Value out of allowed range")
        if isinstance(result, Fraction):
            return float(result)
        return result

    def _evaluate_parsed_expression(self, parsed_expression):
        if isinstance(parsed_expression, (int, Fraction)):
            return parsed_expression
        elif self._is_monomial_expression(parsed_expression):
            return self._evaluate_monomial_expression(parsed_expression)
        else:
            return self._evaluate_polynomial_expression(parsed_expression)

    def _is_monomial_expression(self, parsed_expression):
        return len(parsed_expression) == self.SINGLE_OPERAND_LENGTH

    def _evaluate_monomial_expression(self, parsed_expression):
        return self._evaluate_parsed_expression(parsed_expression[self.FIRST_OPERAND_INDEX])

    def _evaluate_polynomial_expression(self, parsed_expression):
        left = self._evaluate_parsed_expression(parsed_expression[self.FIRST_OPERAND_INDEX])
        op = parsed_expression[self.OPERATOR_INDEX]
        right = self._evaluate_parsed_expression(parsed_expression[self.SECOND_OPERAND_INDEX])
        return self.operator.execute(op, left, right)
