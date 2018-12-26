# -*- coding: utf-8 -*-
"""
Opens IDEs...
"""

import os


class Py3status:

    def __init__(self):
        self.selected = 0
        self.tools_text = ['PC', 'IJ', 'GO', 'PS', 'WS']
        self.tools = {'PC': 'pycharm', 'IJ': 'idea', 'GO': 'goland', 'PS': 'phpstorm', 'WS': 'webstorm'}
        self._parse_text()
        self.amount = 5

    def _parse_text(self):
        s = ""
        for idx, tool in enumerate(self.tools_text):
            if idx == self.selected:
                s += "(" + tool + ")"
            else:
                s += " " + tool + " "
        self.full_text = 'JetBrains: ' + s

    def on_click(self, event):
        button = event['button']
        if button == 4:
            if self.selected == 0:
                self.selected = self.amount - 1
            else:
                self.selected -= 1
            self._parse_text()
        if button == 5:
            self.selected = (self.selected + 1) % self.amount
            self._parse_text()
        if button == 1:
            os.system('exec ' + self.tools[self.tools_text[self.selected]] + ' &')

    def icons(self):
        return {
            'full_text': self.full_text,
            'cached_until': self.py3.CACHE_FOREVER
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
