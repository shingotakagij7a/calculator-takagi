from calculator_cli.service.evaluate_service import EvaluateService


class CalculatorController:
    def __init__(self, calculator_view):
        self.view = calculator_view
        self.evaluator = EvaluateService()

    def evaluate_and_display(self, expression):
        try:
            result = self.evaluator.execute(expression)
            self.view.output_result(result)
        except ValueError as e:
            return str(e)
