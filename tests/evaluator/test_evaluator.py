import pytest

from calculator_cli.evaluator.evaluator import Evaluator


class TestEvaluator:
    @pytest.mark.parametrize(
        ["input", "expected"],
        [
            pytest.param("0", 0, id="single operand"),
            pytest.param("1 + 2", 3, id="addition"),
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

    class Test_文字列の算術演算式の入力が不適切な場合に例外を送出する:
        @pytest.mark.parametrize(
            ["input", "expected_exception", "expected_message"],
            [
                pytest.param("1 > 0", ValueError, "Invalid expression", id="comparison operator"),
            ]
        )
        def test_使用不可能な演算子が含まれている場合に例外を発生させる(self, input, expected_exception, expected_message):
            evaluator = Evaluator()
            with pytest.raises(expected_exception, match=expected_message):
                evaluator.execute(input)
