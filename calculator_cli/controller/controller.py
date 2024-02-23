from calculator_cli.evaluator.evaluator import Evaluator


class Controller:
    def __init__(self):
        self.evaluator = Evaluator()

    def evaluate_expression(self, expression):
        try:
            result = self.evaluator.execute(expression)
            return result
        except ValueError as e:
            return str(e)
