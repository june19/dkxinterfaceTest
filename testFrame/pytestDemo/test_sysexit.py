#-*- coding:utf-8 -*-
#@ Time :2020.11.16
#@Author :tanglijun
#@file test_sysexit.py
#@project :pythonTestDemo

import pytest
def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()
