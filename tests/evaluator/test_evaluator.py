import pytest

from calculator_cli.evaluator.evaluator import Evaluator


class TestEvaluator:
    @pytest.mark.parametrize(
        ["input", "expected"],
        [
            pytest.param("0", 0, id="single operand"),
            pytest.param("1 + 2", 3, id="addition"),
            # pytest.param("1 - 2", -1, id="subtraction"),
            # pytest.param("1 - 2 * 3", -5, id="combination of subtraction and multiplication"),
            # pytest.param("(1 - 2) * 3", -3, id="combination of subtraction and multiplication with parentheses"),
        ]
    )
    def test_文字列の算術演算式の入力が適切な場合にその計算結果の数値を返す(self, input, expected):
        evaluator = Evaluator()
        assert evaluator.evaluate(input) == expected

    # class Test_文字列の算術演算式の入力が不適切な場合に例外を送出する:
    #     @pytest.mark.parametrize(
    #         ["input", "expected"],
    #         [
    #             pytest.param("1 > 0", ValueError, id="comparison operator"),
    #         ]
    #     )
    #     def test_使用不可能な演算子が含まれている場合に例外を発生させる(self, input, expected):
    #         evaluator = Evaluator()
    #         with pytest.raises(Exception, match=expected):
    #             evaluator.evaluate(input)
