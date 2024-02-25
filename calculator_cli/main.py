import argparse
import sys

from calculator_cli.controller.controller import Controller
from calculator_cli.view.calculator_view import CalculatorView


def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("--scale", type=int, default=None, help="Scale for rounding the result")
    parser.add_argument("expression", type=str, nargs="?", default="", help="Mathematical expression to evaluate")

    args = parser.parse_args()
    print(args.expression)
    controller = Controller()
    view = CalculatorView(scale=args.scale)

    if args.interactive:
        run_interactive_mode(controller, view)
    else:
        if args.expression:
            result = controller.evaluate_expression(args.expression)
            print(view.format_result(result))
        else:
            print("No expression provided. Exiting.")
            sys.exit(1)


def run_interactive_mode(controller, view):
    print("Entering interactive mode. Type 'exit' to exit.")
    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == "exit":
                break
            result = controller.evaluate_expression(expression)
            print(view.format_result(result))
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
