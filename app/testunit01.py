import flask_test
import unittest

def test_calc():
    result = flask_test.calc()
    assert 30000 >= result

def test_msg():
    msg = flask_test.funcmsg()
    assert "testmessage" == msg
