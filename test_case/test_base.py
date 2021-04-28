#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/28 21:23
# @Author   : InsaneLoafer
# @File     : test_base.py
from page.app import App

class TestBase:
    app = None
    def setup(self):
        self.app = App()