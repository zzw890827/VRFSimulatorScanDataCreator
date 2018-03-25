#!/usr/bin/python3

"""メインアプリ

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-19T14:40:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

import sys
from PyQt5.QtWidgets import QApplication
from view import DialogWelcome


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DialogWelcome()
    ui.show()
    sys.exit(app.exec_())
