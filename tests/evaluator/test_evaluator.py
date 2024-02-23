import pytest

from calculator_cli.evaluator.evaluator import Evaluator


class TestEvaluator:
    class Test正常系:
        @pytest.mark.parametrize(
            ["input", "expected"],
            [
                pytest.param("0", 0, id="single operand"),
                pytest.param("1 + 2", 3, id="addition"),
                pytest.param("1+2", 3, id="addition without space"),
                pytest.param("1 +    2", 3, id="addition with multiple spaces"),
                pytest.param("1 - 2", -1, id="subtraction"),
                pytest.param("1 - 2 * 3", -5, id="combination of subtraction and multiplication"),
                pytest.param("(1 - 2) * 3", -3, id="combination of subtraction and multiplication with parentheses"),
                pytest.param("0.1 + 0.2", 0.3, id="addition of floating point numbers"),
                pytest.param("10 / 3", 3.3333333333333335, id="division of integers with floating point result"),
            ]
        )
        def test_文字列の算術演算式の入力が適切な場合にその計算結果の数値を返す(self, input, expected):
            evaluator = Evaluator()
            assert evaluator.execute(input) == expected

    class Test異常系_文字列の算術演算式の入力が不適切:
        @pytest.mark.parametrize(
            ["input", "expected_exception", "expected_message"],
            [
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
            evaluator = Evaluator()
            with pytest.raises(expected_exception, match=expected_message):
                evaluator.execute(input)
