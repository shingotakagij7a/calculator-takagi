import argparse

from calculator_cli.controller.calculator_controller import \
    CalculatorController
from calculator_cli.view.calculator_view import CalculatorView

WAITING_FOR_EXPRESSION = ">>> "
EXIT_EXPRESSION = "exit"
INTERACTIVE_MODE_MESSAGE = "Entering interactive mode. Type 'exit' to exit."
NO_EXPRESSION_MESSAGE = "No expression provided. Enter an expression to evaluate."


def evaluate_and_display(expression, controller, view):
    if not expression:
        print(NO_EXPRESSION_MESSAGE)
        return
    try:
        result = controller.evaluate_expression(expression)
        view.output_result(result)
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("-s", "--scale", type=int, default=None, help="Scale for rounding the result")
    parser.add_argument("expression", type=str, nargs="?", default="", help="Mathematical expression to evaluate")
    args = parser.parse_args()

    controller = CalculatorController()
    view = CalculatorView(scale=args.scale)

    if args.interactive:
        print(INTERACTIVE_MODE_MESSAGE)
        while True:
            expression = input(WAITING_FOR_EXPRESSION)
            if expression.lower() == EXIT_EXPRESSION:
                break
            evaluate_and_display(expression, controller, view)
    else:
        evaluate_and_display(args.expression, controller, view)


if __name__ == "__main__":
    main()
