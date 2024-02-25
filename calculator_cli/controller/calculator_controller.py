from calculator_cli.service.evaluate_service import EvaluateService


class CalculatorController:
    def __init__(self):
        self.evaluator = EvaluateService()

    def evaluate_expression(self, expression):
        try:
            result = self.evaluator.execute(expression)
            return result
        except ValueError as e:
            return str(e)
