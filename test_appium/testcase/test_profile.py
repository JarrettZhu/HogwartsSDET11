import pytest

from test_appium.page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().start().main().goto_profile()

    @pytest.mark.parametrize("phone, password", [
        ("13424103317", "123456")
    ])
    def test_login_by_password(self, phone, password):
        assert "错误" in self.profile.login_by_password(phone, password)
