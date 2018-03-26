#!/usr/bin/python3

"""試験項目ウィザードビュー

試験項目ウィザードクラス及び関連するメソッドやSiｇnalとSlotの定義

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-19T19:27:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont, QImage, QPixmap

from ui import Ui_Dialog_items

from view import DialogMaterSlaveTest


class DialogItems(QWidget, Ui_Dialog_items):
    """試験項目ウィザードクラス

    """

    def __init__(self):
        super(DialogItems, self).__init__()
        self.setupUi(self)
        self.default_font = '游ゴシック 本文'
        self.icon_path = 'resources/icons/wizard.png'

        radio_table = [self.radio_1_items, self.radio_2_items,
                       self.radio_3_items, self.radio_4_items,
                       self.radio_5_items]

        label_table = [self.label_1_radio_items,
                       self.label_2_radio_items,
                       self.label_3_radio_items,
                       self.label_4_radio_items,
                       self.label_5_radio_items]

        # フォント
        for e in radio_table:
            e.setFont(QFont(self.default_font))
            e.setStyleSheet('font: 14px')

        for e in label_table:
            e.setFont(QFont(self.default_font))
            e.setStyleSheet('font: 14px')

        self.btn_create_items.setFont(QFont(self.default_font))
        self.btn_detail_items.setFont(QFont(self.default_font))
        self.btn_cancel_items.setFont(QFont(self.default_font))

        # アイコン
        # http://www.mylessonplanner.com/clickbank/1/?hop=bzznora
        self.image = QImage(self.icon_path)
        self.label_pic_items.setAlignment(Qt.AlignCenter)
        self.label_pic_items.setAutoFillBackground(True)
        self.label_pic_items.setPixmap(QPixmap.fromImage(self.image))

        self.setFixedSize(self.width(), self.height())  # サイズ変更禁止

        # 親子機画面
        self.next_page_master = DialogMaterSlaveTest()

        # Signal
        # キャンセルボタン
        self.btn_cancel_items.clicked.connect(QCoreApplication.quit)
        # 作成ボタン
        self.btn_create_items.clicked.connect(
            lambda: self.btn_clicked_event_create(1))
        # 詳細ボタン
        self.btn_detail_items.clicked.connect(
            self.btn_clicked_event_detail)

    # Slot
    def btn_clicked_event_create(self, n):
        """作成ボタンスロット関数

        作成ボタンを押下時の動き

        Args:
            n: 作成データの種類

        Returns:
            VRFシミュレーター用データ
        """
        # create_vrf_system_data(n)
        self.close()

    def btn_clicked_event_detail(self):
        """詳細ボタンスロット関数

        詳細ボタンを押下時の動き
        """
        self.next_page_master.show()
        self.close()
