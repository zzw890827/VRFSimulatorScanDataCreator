#!/usr/bin/python3

"""完了ウィザードビュー

試験項目ウィザードクラス及び関連するメソッドやSiｇnalとSlotの定義

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-19T21:24:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QImage, QPixmap
from PyQt5.QtCore import QBasicTimer, QCoreApplication, Qt

from ui import Ui_Dialog_finish


class DialogFinish(QWidget, Ui_Dialog_finish):
    """完了ウィザードクラス

    """

    def __init__(self):
        super(DialogFinish, self).__init__()
        self.setupUi(self)

        self.icon_path = 'resources/icons/wizard.png'
        self.default_font = '游ゴシック 本文'
        self.step = 0
        self.timer = QBasicTimer()  # タイマーを初期化

        # フォント
        self.label_finish.setStyleSheet('font: 14px')
        self.label_finish.setFont(QFont(self.default_font))
        self.progressBar.setFont(QFont(self.default_font))
        self.btn_finish.setFont(QFont(self.default_font))

        # アイコン
        # http://www.mylessonplanner.com/clickbank/1/?hop=bzznora
        self.image = QImage(self.icon_path)
        self.label_pic_finish.setAlignment(Qt.AlignCenter)
        self.label_pic_finish.setAutoFillBackground(True)
        self.label_pic_finish.setPixmap(QPixmap.fromImage(self.image))

        self.setFixedSize(self.width(), self.height())  # サイズ変更禁止

        # Signal
        # 完了ボタン
        self.btn_finish.clicked.connect(QCoreApplication.quit)

    def timerEvent(self, a0: 'QTimerEvent'):
        """タイマーイベント

        プロセスバー用タイマー

        """
        if self.step >= 100:
            self.timer.stop()
            self.btn_finish.setEnabled(True)  # 完了ボタン有効化
            return

        self.step = self.step + 10
        self.progressBar.setValue(self.step)

    def start_process_bar(self):
        """プロセスバーを開始

        完了ボタン無効化、タイマーを開始
        """
        self.btn_finish.setEnabled(False)
        self.step = 0
        self.timer.start(100, self)
