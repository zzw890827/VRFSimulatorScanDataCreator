#!/usr/bin/python3

"""室内機機能

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-21T14:40:21+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'


class ExistTestFunction(object):
    """機能有無テスト用機能クラス

    Attributes:
        auto_save: (0) Auto Save
        auto_on_off: (1) Auto On/Off
        auto_off: (2) Auto Off
        economic: (3) 省エネ機能
        anti_freeze: (4) 除霜機能
        filter_sign: (5) フィルタリングサイン機能
        central: (6) セントラ機能
        highhigh: (7) 風量Hi-Hi機能
        mediumhigh: (8) 風量me-hi機能
        lowlow: (9) 風量Lo-Lo機能
        fan_auto: (10) 風量Auto機能
        fan_high: (11) 風量High機能
        fan_quiet: (12) 風量Quiet機能
        vt_1: (13) 1番
        vt_2: (14) 2番
        vt_3: (15) 3番
        vt_4: (16) 4番
        ht_1: (17) 1番
        ht_2: (18) 2番
        ht_3: (19) 3番
        ht_4: (20) 4番

    """

    def __init__(self):
        self.auto_save = ['HSAutoSaveFunction', 'Exist']
        self.auto_on_off = ['HSAutoOnOffFunction', 'Exist']
        self.auto_off = ['HSAutoOffFunction', 1]
        self.economic = ['EnergySaveFucntion', 'Exist']
        self.anti_freeze = ['Anti-FreezeFunction', 'Exist']
        self.filter_sign = ['FilterSignClearFunction', 'Exist']
        self.central = ['CentralFunction', 'Exist']
        self.highhigh = ['FanLevelHighHigh', 'Exist']
        self.mediumhigh = ['FanLevelMedHigh', 'Exist']
        self.lowlow = ['FanLevelLowLow', 'Exist']
        self.fan_auto = ['FanLevelAuto', 'Exist']
        self.fan_high = ['FanLevelHigh', 'Exist']
        self.fan_quiet = ['FanLevelQuiet', 'Exist']
        self.vt_1 = ['LouverVT1AvailableSteps', 4]
        self.vt_2 = ['LouverVT2AvailableSteps', 4]
        self.vt_3 = ['LouverVT3AvailableSteps', 4]
        self.vt_4 = ['LouverVT4AvailableSteps', 4]
        self.ht_1 = ['LouverHT1AvailableSteps', 4]
        self.ht_2 = ['LouverHT2AvailableSteps', 4]
        self.ht_3 = ['LouverHT3AvailableSteps', 4]
        self.ht_4 = ['LouverHT4AvailableSteps', 4]

    def change_existence(self, idx, sensor=0):
        """機能有にきりかえ

        Args:
            idx: 機能インデックス
            sensor: auto off レベル

        """
        function_list = [self.auto_save, self.auto_on_off,
                         self.auto_off, self.economic, self.anti_freeze,
                         self.filter_sign, self.central, self.highhigh,
                         self.mediumhigh, self.lowlow, self.fan_auto,
                         self.fan_high, self.fan_quiet, self.vt_1,
                         self.vt_2, self.vt_3, self.vt_4, self.ht_1,
                         self.ht_2, self.ht_3, self.ht_4]
        if 13 <= idx <= 20:
            function_list[idx][1] = 4
            return
        if idx == 2:
            function_list[idx][1] = sensor
            return
        function_list[idx][1] = 'Exist'

    def change_none(self, idx):
        """機能なしにきりかえ

        Args:
            idx: 機能インデックス
            sensor: auto off レベル

        """
        function_list = [self.auto_save, self.auto_on_off,
                         self.auto_off, self.economic, self.anti_freeze,
                         self.filter_sign, self.central, self.highhigh,
                         self.mediumhigh, self.lowlow, self.fan_auto,
                         self.fan_high, self.fan_quiet, self.vt_1,
                         self.vt_2, self.vt_3, self.vt_4, self.ht_1,
                         self.ht_2, self.ht_3, self.ht_4]
        if 13 <= idx <= 20 or idx == 2:
            function_list[idx][1] = 0
            return
        function_list[idx][1] = 'None'

    def get_function(self, idx):
        """機能情報を取得

        Args:
            idx: 機能インデックス
        Returns:
            機能式
        """
        function_list = [self.auto_save, self.auto_on_off,
                         self.auto_off, self.economic, self.anti_freeze,
                         self.filter_sign, self.central, self.highhigh,
                         self.mediumhigh, self.lowlow, self.fan_auto,
                         self.fan_high, self.fan_quiet, self.vt_1,
                         self.vt_2, self.vt_3, self.vt_4, self.ht_1,
                         self.ht_2, self.ht_3, self.ht_4]

        if 13 <= idx <= 20 or idx == 2:
            return function_list[idx][0] + '=' + str(
                function_list[idx][1])
        return function_list[idx][0] + '=' + function_list[idx][1]
