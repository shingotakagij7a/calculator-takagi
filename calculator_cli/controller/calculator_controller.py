from calculator_cli.service.calculator_service import CalculatorService


class CalculatorController:
    def __init__(self, calculator_view):
        self.view = calculator_view
        self.service = CalculatorService()

    def evaluate_and_display(self, expression):
        try:
            result = self.service.calculate(expression)
            self.view.output_result(result)
        except ValueError as e:
            return str(e)
