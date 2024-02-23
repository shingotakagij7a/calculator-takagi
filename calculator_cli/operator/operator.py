class Operator:
    def __init__(self):
        self.operations = {
            '+': lambda left, right: left + right,
            '-': lambda left, right: left - right,
            '*': lambda left, right: left * right,
            '/': lambda left, right: left / right,
        }

    def execute(self, op_symbol, left, right):
        if op_symbol in self.operations:
            return self.operations[op_symbol](left, right)
        raise ValueError(f"Unsupported operation: {op_symbol}")
