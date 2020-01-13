import pytest

from unit.div import div


class Testjob1:

    # 参数化，遇到assert错误不会直接退出，更灵活
    @pytest.mark.happy
    @pytest.mark.parametrize("number_1, number_2, expection", {
        (10, 2, 5),
        (10, 5, 3),
        (1000000, 1, 1000000),
        (100, 200, 0.5)
    })
    def test_div_int_param(self, number_1, number_2, expection):
        assert div(number_1, number_2) == expection

    @pytest.mark.happy
    @pytest.mark.parametrize("float_number_1, float_number_2, expection", {
        (10, 3, 3.3333333),
        (10.2, 0.2, 51)
    })
    def test_div_float(self, float_number_1, float_number_2, expection):
        assert div(float_number_1, float_number_2) == expection

    @pytest.mark.exception
    @pytest.mark.parametrize("value_1, value_2", {
        (10, 'a'),
        ('abc', 10)
    })
    def test_div_exception(self, value_1, value_2):
        assert div(value_1, value_2)

    @pytest.mark.happy
    @pytest.mark.parametrize("value_1, zero, expection", {
        (10, 0, None)
    })
    def test_div_zero(self, value_1, zero, expection):
        assert div(value_1, zero) == expection

    # 预期出现除0错误异常
    @pytest.mark.exception
    @pytest.mark.parametrize("value_1, value_2", {
        (1, 0)
    })
    def test_zero_division(self, value_1, value_2):
        with pytest.raises(ZeroDivisionError):
            value_1 / value_2
