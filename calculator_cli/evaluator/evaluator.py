from calculator_cli.operator.operator import Operator
from calculator_cli.parser.parser import Parser


class Evaluator:
    SINGLE_OPERAND_LENGTH = 1
    FIRST_OPERAND_INDEX = 0
    OPERATOR_INDEX = 1
    SECOND_OPERAND_INDEX = 2

    def __init__(self):
        self.operator = Operator()
        self.parser = Parser()

    def execute(self, expression):
        parsed_expression = self.parser.execute(expression)
        return self._evaluate_parsed_expression(parsed_expression)

    def _evaluate_parsed_expression(self, parsed_expression):
        if isinstance(parsed_expression, int):
            return parsed_expression
        elif self.is_monomial_expression(parsed_expression):
            return self._evaluate_monomial_expression(parsed_expression)
        else:
            return self._evaluate_polynomial_expression(parsed_expression)

    def is_monomial_expression(self, parsed_expression):
        return len(parsed_expression) == self.SINGLE_OPERAND_LENGTH

    def _evaluate_monomial_expression(self, parsed_expression):
        return self._evaluate_parsed_expression(parsed_expression[self.FIRST_OPERAND_INDEX])

    def _evaluate_polynomial_expression(self, parsed_expression):
        left = self._evaluate_parsed_expression(parsed_expression[self.FIRST_OPERAND_INDEX])
        op = parsed_expression[self.OPERATOR_INDEX]
        right = self._evaluate_parsed_expression(parsed_expression[self.SECOND_OPERAND_INDEX])
        return self.operator.execute(op, left, right)
