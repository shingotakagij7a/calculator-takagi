import pytest

from calculator_cli.service.calculator_service import CalculatorService


class TestCalculatorService:
    class Test正常系:
        @pytest.mark.parametrize(
            ["input", "expected"],
            [
                pytest.param("0", 0, id="single operand"),
                pytest.param("1 + 2", 3, id="addition"),
                pytest.param("3 + 8 + 8", 19, id="addition with multiple operands"),
                pytest.param("1+2", 3, id="addition without space"),
                pytest.param("1 +    2", 3, id="addition with multiple spaces"),
                pytest.param("1 - 2", -1, id="subtraction"),
                pytest.param("1 - 2 * 3", -5, id="combination of subtraction and multiplication"),
                pytest.param("(1 - 2) * 3", -3, id="combination of subtraction and multiplication with parentheses"),
                pytest.param("0.1 + 0.2", 0.3, id="addition of floating point numbers"),
                pytest.param("10 / 3", 3.3333333333333335, id="division of integers with floating point result"),
                pytest.param("2 * 2 * 2", 8, id="multiple multiplications"),
                pytest.param("2 * (3 + 3)", 12, id="combination with parentheses"),
                pytest.param("-1 + 2", 1, id="negative number addition"),
                pytest.param("2.5 * 4", 10.0, id="multiplication with floating point number"),
                pytest.param("3.5 - 1.5", 2.0, id="subtraction of floating point numbers"),
                pytest.param("4 / 2", 2, id="division resulting in integer"),
                pytest.param("(2 + 3) * (2 - 1)", 5, id="nested parentheses")
            ]
        )
        def test_文字列の算術演算式の入力が適切な場合にその計算結果の数値を返す(self, input, expected):
            service = CalculatorService()
            assert service.calculate(input) == expected

    class Test異常系_文字列の算術演算式の入力が不適切:
        @pytest.mark.parametrize(
            ["input", "expected_exception", "expected_message"],
            [
                pytest.param("1 / 0", ValueError, "Division by zero", id="division by zero"),
                pytest.param("1 > 0", ValueError, "Contains operator not allowed", id="comparison operator"),
                pytest.param("+", ValueError, "Ends with operator", id="single operator"),
                pytest.param("1 +", ValueError, "Ends with operator", id="single operand and operator"),
                pytest.param("1 + * 2", ValueError, "Other invalid expression", id="continuous operators"),
                pytest.param("(1 + 2", ValueError, "Other invalid expression", id="unmatched parentheses"),
                pytest.param("1 + 1000000001", ValueError, "Value out of allowed range", id="large number"),
                pytest.param("1 + -1000000001", ValueError, "Value out of allowed range", id="small number"),
            ]
        )
        def test_文字列の算術演算式の入力が不適切な場合に例外を送出する(self, input, expected_exception, expected_message):
            service = CalculatorService()
            with pytest.raises(expected_exception, match=expected_message):
                service.calculate(input)

    class Test異常系_算術結果の出力が不適切:
        @pytest.mark.parametrize(
            ["input", "expected_exception", "expected_message"],
            [
                pytest.param("2 + 999999999", ValueError, "Value out of allowed range", id="large number"),
                pytest.param("-2 - 999999999", ValueError, "Value out of allowed range", id="small number"),
            ]
        )
        def test_文字列の算術演算式の入力が不適切な場合に例外を送出する(self, input, expected_exception, expected_message):
            service = CalculatorService()
            with pytest.raises(expected_exception, match=expected_message):
                service.calculate(input)
