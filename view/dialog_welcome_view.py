#!/usr/bin/python3

"""ウェルカムウィザードビュー

ウェルカムウィザードクラス及び関連するメソッドやSiｇnalとSlotの定義

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-19T14:40:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont, QImage, QPixmap

from ui import Ui_Dialog_welcome

from view import DialogItems


class DialogWelcome(QWidget, Ui_Dialog_welcome):
    """ウェルカムウィザードクラス

    """

    def __init__(self):
        super(DialogWelcome, self).__init__()
        self.setupUi(self)
        self.default_font = '游ゴシック 本文'
        self.icon_path = 'resources/icons/wizard.png'

        # フォント
        self.label_1_welcome.setStyleSheet('font: 40px')
        self.label_1_welcome.setFont(QFont(self.default_font))
        self.label_2_welcome.setStyleSheet('font: 14px')
        self.label_2_welcome.setFont(QFont(self.default_font))
        self.label_3_welcome.setStyleSheet('font: 14px')
        self.label_3_welcome.setFont(QFont(self.default_font))

        # ボタン
        self.btn_cancel_welcome.setFont(QFont(self.default_font))
        self.btn_next_welcome.setFont(QFont(self.default_font))

        self.setFixedSize(self.width(), self.height())  # サイズ変更禁止

        # アイコン
        # http://www.mylessonplanner.com/clickbank/1/?hop=bzznora
        self.image = QImage(self.icon_path)
        self.label_pic_welcome.setAlignment(Qt.AlignCenter)
        self.label_pic_welcome.setAutoFillBackground(True)
        self.label_pic_welcome.setPixmap(QPixmap.fromImage(self.image))

        # Items画面
        self.next_page=DialogItems()

        # Signal
        # キャンセルボタン
        self.btn_cancel_welcome.clicked.connect(QCoreApplication.quit)
        # 次へボタン
        self.btn_next_welcome.clicked.connect(
            self.btn_clicked_event_next)

    # Slot
    # 次へボタン
    def btn_clicked_event_next(self):
        """次へボタンスコット関数

        次へボタンを押下時の動き
        """
        self.next_page.show()
        self.close()
