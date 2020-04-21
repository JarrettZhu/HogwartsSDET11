from test_requests.test_wework.api.wework import WeWork


class TestWeWork:


    @classmethod
    def setup_class(cls):
        cls.token = WeWork.get_token()

    def test_get_token(self):
        r = WeWork.get_access_token(WeWork.secret)
        self.token = r["access_token"]

    def test_get_token_exist(self):
        assert self.token is not None
