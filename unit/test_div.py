import pytest

from unit.div import div


class Testjob1:
    # 缺点，assert错误马上退出，不会执行后续的断言
    @pytest.mark.happy
    def test_div_int(self):
        assert div(10, 5) == 2
        assert div(10, 2) == 5
        assert div(1000000, 1) == 1000000

    # 参数化，遇到assert错误不会直接退出，更灵活
    @pytest.mark.happy
    @pytest.mark.parametrize("number1, number2, expection", {
        (10, 2, 5),
        (10, 5, 3),
        (1000000, 1, 1000000),
        (100, 200, 0.5)
    })
    def test_div_int_param(self, number1, number2, expection):
        assert div(number1, number2) == expection

    @pytest.mark.happy
    def test_div_float(self):
        assert div(10, 3) == 3.3333333
        assert div(10.2, 0.2) == 51

    @pytest.mark.exception
    def test_div_exception(self):
        assert div(10, 'a')
        assert div('abc', 10)

    @pytest.mark.happy
    def test_div_zero(self):
        assert div(10, 0) == None

    # 预期出现除0错误异常
    @pytest.mark.exception
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
