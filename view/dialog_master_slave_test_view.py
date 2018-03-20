#!/usr/bin/python3

"""親機子機テストウィザードビュー

親機子機テストウィザードクラス及び関連するメソッドやSiｇnalとSlotの定義

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-20T10:13:40+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from PyQt5.QtCore import QRect, Qt, QCoreApplication
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem

from ui import Ui_Dialog_master_slave_test


class DialogMaterSlaveTest(QWidget, Ui_Dialog_master_slave_test):
    def __init__(self):
        super(DialogMaterSlaveTest, self).__init__()
        self.setupUi(self)
        self.default_font = '游ゴシック 本文'
        self.latin_font = 'Arial'
        self.icon_path = 'resources/icons/wizard.png'
        self.check_path = 'resources/icons/check.png'
        self.minus_path = 'resources/icons/minus.png'

        self.exist_table = [(1, 0), (1, 1), (2, 0), (3, 1)]
        self.none_table = [(2, 1), (3, 0), (4, 0), (4, 1)]

        # 説明ラベル
        self.label_master_slave.setStyleSheet('font: 15px')
        self.label_master_slave.setFont(QFont(self.default_font))

        # アイコン
        # http://www.mylessonplanner.com/clickbank/1/?hop=bzznora
        self.image = QImage(self.icon_path)
        self.label_pic_master_slave.setAlignment(Qt.AlignCenter)
        self.label_pic_master_slave.setAutoFillBackground(True)
        self.label_pic_master_slave.setPixmap(
            QPixmap.fromImage(self.image))

        self.setFixedSize(self.width(), self.height())  # サイズ変更禁止

        # ==================風量グループ===================
        strength_group = [self.group_fan_strength_auto,
                          self.group_fan_strength_high,
                          self.group_fan_strength_quiet]
        strength_table = [self.table_fan_strength_auto,
                          self.table_fan_strength_high,
                          self.table_fan_strength_quiet]
        self.strength_check = [self.check_fan_strength_auto,
                               self.check_fan_strength_high,
                               self.check_fan_strength_quiet]
        # 子グループ設置
        self.locate_group(strength_group,
                          strength_table,
                          self.strength_check)
        # 親グループ
        self.group_fan_strength.setStyleSheet('font: 16px')
        self.group_fan_strength.setFont(QFont(self.default_font))
        self.group_fan_strength.setGeometry(
            QRect(20, 80, 306, 200))

        # ====================新風量グループ===================
        new_strength_group = [self.group_fan_new_strength_hihi,
                              self.group_fan_new_strength_mehi,
                              self.group_fan_new_strength_lolo]
        new_strength_table = [self.table_fan_new_strength_hihi,
                              self.table_fan_new_strength_mehi,
                              self.table_fan_new_strength_lolo]
        self.new_strength_check = [self.check_fan_new_strength_hihi,
                                   self.check_fan_new_strength_mehi,
                                   self.check_fan_new_strength_lolo]
        # 子グループ設置
        self.locate_group(new_strength_group,
                          new_strength_table,
                          self.new_strength_check)

        # 親グループ
        self.group_fan_new_strength.setStyleSheet('font: 16px')
        self.group_fan_new_strength.setFont(QFont(self.default_font))
        self.group_fan_new_strength.setGeometry(
            QRect(340, 80, 306, 200))

        # ===============左右風向板グループ===================
        horizontal_group = [self.group_horizontal_1,
                            self.group_horizontal_2,
                            self.group_horizontal_3,
                            self.group_horizontal_4]
        horizontal_table = [self.table_horizontal_1,
                            self.table_horizontal_2,
                            self.table_horizontal_3,
                            self.table_horizontal_4]
        self.horizontal_check = [self.check_horizontal_1,
                                 self.check_horizontal_2,
                                 self.check_horizontal_3,
                                 self.check_horizontal_4]
        # 子グループ設置
        self.locate_group(horizontal_group,
                          horizontal_table,
                          self.horizontal_check)

        # 親グループ
        self.group_horizontal.setStyleSheet('font: 16px')
        self.group_horizontal.setFont(QFont(self.default_font))
        self.group_horizontal.setGeometry(
            QRect(20, 300, 406, 200))

        # ===============上下風向板グループ===================
        vertical_group = [self.group_vertical_1,
                          self.group_vertical_2,
                          self.group_vertical_3,
                          self.group_vertical_4]
        vertical_table = [self.table_vertical_1,
                          self.table_vertical_2,
                          self.table_vertical_3,
                          self.table_vertical_4]
        self.vertical_check = [self.check_vertical_1,
                               self.check_vertical_2,
                               self.check_vertical_3,
                               self.check_vertical_4]

        # 子グループ設置
        self.locate_group(vertical_group,
                          vertical_table,
                          self.vertical_check)

        # 親グループ
        self.group_vertical.setStyleSheet('font: 16px')
        self.group_vertical.setFont(QFont(self.default_font))
        self.group_vertical.setGeometry(QRect(440, 300, 406, 200))

        # ===============その他グループ===================
        other_group = [self.group_eco,
                       self.group_anti,
                       self.group_test,
                       self.group_filter]
        other_table = [self.table_eco,
                       self.table_anti,
                       self.table_test,
                       self.table_filter]
        self.other_check = [self.check_eco,
                            self.check_anti,
                            self.check_test,
                            self.check_filter]

        # 子グループ設置
        self.locate_group(other_group,
                          other_table,
                          self.other_check)

        # 親グループ
        self.group_other.setStyleSheet('font: 16px')
        self.group_other.setFont(QFont(self.default_font))
        self.group_other.setGeometry(QRect(660, 80, 406, 200))

        # ===============人感センサーグループ===================
        sensor_group = [self.group_auto_save,
                        self.group_auto_on_off,
                        self.group_auto_off]
        sensor_table = [self.table_auto_save,
                        self.table_auto_on_off,
                        self.table_auto_off]
        self.sensor_check = [self.check_auto_save,
                             self.check_auto_on_off,
                             self.check_auto_off]
        # 子グループ設置
        self.locate_group(sensor_group,
                          sensor_table,
                          self.sensor_check)

        # 親グループ
        self.group_sensor.setStyleSheet('font: 16px')
        self.group_sensor.setFont(QFont(self.default_font))
        self.group_sensor.setGeometry(
            QRect(860, 300, 362, 230))

        # Auto Offにおける特別な処理
        self.group_auto_off.setGeometry(QRect(210, 20, 142, 194))
        self.table_auto_off.setGeometry(QRect(10, 20, 122, 140))
        self.table_auto_off.setColumnWidth(0, 60)
        self.table_auto_off.setColumnWidth(1, 60)
        item = QTableWidgetItem('Lv2')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(1, 0, item)
        item = QTableWidgetItem('Lv2')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(1, 1, item)
        item = QTableWidgetItem('Lv2')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(2, 0, item)
        item = QTableWidgetItem('Lv1')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(2, 1, item)
        item = QTableWidgetItem('Lv2')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(3, 1, item)
        item = QTableWidgetItem('Lv1')
        item.setIcon(QIcon(self.check_path))
        self.table_auto_off.setItem(4, 0, item)
        item = QTableWidgetItem()
        item.setIcon(QIcon(self.minus_path))
        self.table_auto_off.setItem(5, 0, item)
        item = QTableWidgetItem()
        item.setIcon(QIcon(self.minus_path))
        self.table_auto_off.setItem(5, 1, item)
        self.check_auto_off.setGeometry(QRect(66, 168, 16, 16))

        # signal
        # キャンセルボタン
        self.btn_cancel_master_slave.clicked.connect(
            QCoreApplication.quit)
        # 全選択ボタン
        self.btn_select_all_master_slave.clicked.connect(
            lambda: self.change_check_box_status(select_all=True))

    def locate_group(self, group, table, check):
        """子グループを配置

        子グループを親グループに配置

        Args:
             group: 子グループ配列
             table: グループの中のテーブル配列
             check: チェックボックスの配列
        """
        for i in table:
            # 編集無効化
            i.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # 選択無効化
            i.setSelectionMode(QAbstractItemView.NoSelection)
            i.verticalHeader().setVisible(False)  # 垂直ヘッダーを隠す
            i.horizontalHeader().setVisible(False)  # 水平ヘッダーを隠す
            # サイズ合わせ
            i.resizeColumnsToContents()
            i.resizeRowsToContents()
            # フォント
            i.setStyleSheet('font: 14px')
            i.setGeometry(QRect(10, 20, 66, 117))
            # ヘッダー
            item = i.item(0, 0)
            item.setFont(QFont(self.default_font, 14, QFont.Bold))
            item = i.item(0, 1)
            item.setFont(QFont(self.default_font, 14, QFont.Bold))
            # データを埋める
            for j in self.exist_table:  # 機能あり
                item = QTableWidgetItem()
                item.setIcon(QIcon(self.check_path))
                i.setItem(j[0], j[1], item)
            for j in self.none_table:  # 機能無し
                item = QTableWidgetItem()
                item.setIcon(QIcon(self.minus_path))
                i.setItem(j[0], j[1], item)

        # チェックボックスを置く
        for i in check:
            i.setGeometry(QRect(36, 145, 16, 16))

        # 子グループ
        left = 10
        for i in group:
            i.setGeometry(QRect(left, 20, 86, 170))
            left = left + 100
            i.setStyleSheet('font: 16px')
            i.setFont(QFont(self.latin_font))

    # slot関数
    # 全選択及び逆転ボタン
    def change_check_box_status(self, select_all=False):
        check_box_all = (self.sensor_check
                         + self.other_check
                         + self.vertical_check
                         + self.horizontal_check
                         + self.new_strength_check
                         + self.strength_check)
        if select_all:
            for i in check_box_all:
                i.toggle()
