from python_setup_project.main import *


class TestMain(object):

    def test_hello(self):
        result = hello()
        assert 'hello' == result
