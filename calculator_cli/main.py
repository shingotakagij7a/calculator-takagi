import sys

from calculator_cli.controller.controller import Controller


def main():
    controller = Controller()

    if len(sys.argv) != 2:
        print("Usage: python -m calculator_cli '<expression>'")
        sys.exit(1)

    expression = sys.argv[1]
    result = controller.evaluate_expression(expression)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
