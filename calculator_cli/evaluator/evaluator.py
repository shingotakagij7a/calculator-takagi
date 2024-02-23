from calculator_cli.parser.parser import Parser


class Evaluator:
    def __init__(self):
        self.parser = Parser()

    def evaluate(self, expression):
        parsed_expression = self.parser.parse(expression)
        result = 0

        for element in parsed_expression:
            if element.isdigit():
                result += int(element)

        return result
