import allure
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def setup_module():
    print("setup module")


def setup_function():
    print("setup function")


# 报告添加图片
@pytest.mark.img
def test_img():
    assert 123 == 123
    allure.attach.file('C:/Users/Jarrett-zhu/Desktop/12345.jpg', attachment_type=allure.attachment_type.JPG)


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
