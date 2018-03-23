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
# from dialog_items_view import DialogItems
# from view import DialogFinish
from view import DialogMaterSlaveTest
from controller import build_master_slave_test_system
from controller import create_vrf_system_list
from controller import write_csv_file
from model import ExistTestFunction

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ui = DialogMaterSlaveTest()
    ui = DialogWelcome()
    ui.show()
    sys.exit(app.exec_())
    # test = create_vrf_system_list([1, 3, 5])
    # write_csv_file(test, 'test.csv')
