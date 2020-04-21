from pprint import pprint

import requests
from requests import Session, Response

proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

url_get = "https://httpbin.testing-studio.com/get"


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)
    print(r)

    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "cccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      },
                      headers={"h": "header demo"},
                      data={
                          "a": 11,
                          "b": 22,
                          "c": "ccccccccccc"
                      },
                      proxies=proxies,
                      verify=False)
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      files={"file": open("__init__.py", "rb")},
                      proxies=proxies,
                      verify=False
                      )
    print(r.json())
    assert r.status_code == 200


def test_session():
    s = Session()
    s.proxies = proxies
    s.verify = False
    s.get(url_get)


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        # r.content = "OK HOOK SUCCESS"
        r.demo = "demo content"
        return r

    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "cccc"
                     },
                     hooks={"response": [modify_response]})
    print(r.json())
    print(r.demo)
    assert r.status_code == 200
