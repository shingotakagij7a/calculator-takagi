from fractions import Fraction


class CalculatorView:
    DEFAULT_SCALE = 0

    def __init__(self, scale=None):
        self.scale = scale

    def output_result(self, result):
        if self.scale is not None:
            format_spec = f".{self.scale}f"
        else:
            format_spec = f".{self.DEFAULT_SCALE}f"

        if isinstance(result, Fraction):
            result = float(result)

        print(format(result, format_spec))
