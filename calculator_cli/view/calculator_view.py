class CalculatorView:
    def __init__(self, scale=None):
        self.scale = scale

    def format_result(self, result):
        if self.scale is not None and isinstance(result, float):
            format_spec = f".{self.scale}f"
            return format(result, format_spec)
        return str(result)
