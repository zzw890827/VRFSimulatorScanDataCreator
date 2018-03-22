#!/usr/bin/python3

"""室内機機能

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-21T14:40:21+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'
__all__ = ['OtherFunction', 'FanStrength', 'NewFanStrength',
           'LouverVT', 'LouverHT', 'HumanSensor',
           'create_function_table']


class OtherFunction(object):
    """付加機能

    Attributes:
        economic: 省エネ機能
        anti_freeze: 除霜機能
        filter_sign: フィルタリングサイン機能
        central: セントラ機能
    """

    def __init__(self):
        self.economic = ['EnergySaveFucntion', 'Exist']
        self.anti_freeze = ['Anti-FreezeFunction', 'Exist']
        self.filter_sign = ['FilterSignClearFunction', 'Exist']
        self.central = ['CentralFunction', 'Exist']

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.economic, self.anti_freeze,
                      self.filter_sign, self.central]
        func_table[n][1] = False


class FanStrength(object):
    """風量

     Attributes:
         auto: 風量Auto機能
         high: 風量High機能
         quiet: 風量Quiet機能

    """

    def __init__(self):
        self.auto = ['FanLevelAuto', 'Exist']
        self.high = ['FanLevelHigh', 'Exist']
        self.quiet = ['FanLevelQuiet', 'Exist']

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.auto, self.high, self.quiet]
        func_table[n][1] = False


class NewFanStrength(object):
    """新風量

    Attributes:
         highhigh: 風量Hi-Hi機能
         mediumhigh: 風量me-hi機能
         lowlow: 風量Lo-Lo機能

    """

    def __init__(self):
        self.highhigh = ['FanLevelHighHigh', 'Exist']
        self.mediumhigh = ['FanLevelMedHigh', 'Exist']
        self.lowlow = ['FanLevelLowLow', 'Exist']

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.highhigh, self.mediumhigh, self.lowlow]
        func_table[n][1] = False


class LouverVT(object):
    """上下風向板

    Attributes:
        vt_1: 1番
        vt_2: 2番
        vt_3: 3番
        vt_4: 4番
    """

    def __init__(self):
        self.vt_1 = ['LouverVT1AvailableSteps', 4]
        self.vt_2 = ['LouverVT2AvailableSteps', 4]
        self.vt_3 = ['LouverVT3AvailableSteps', 4]
        self.vt_4 = ['LouverVT4AvailableSteps', 4]

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.vt_1, self.vt_2, self.vt_3, self.vt_4]
        func_table[n][1] = 0


class LouverHT(object):
    """左右風向板

    Attributes:
        ht_1: 1番
        ht_2: 2番
        ht_3: 3番
        ht_4: 4番
    """

    def __init__(self):
        self.ht_1 = ['LouverHT1AvailableSteps', 4]
        self.ht_2 = ['LouverHT2AvailableSteps', 4]
        self.ht_3 = ['LouverHT3AvailableSteps', 4]
        self.ht_4 = ['LouverHT4AvailableSteps', 4]

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.ht_1, self.ht_2, self.ht_3, self.ht_4]
        func_table[n][1] = 0


class HumanSensor(object):
    """人感センサ

    Attributes:
        auto_save: Auto Save
        auto_on_off: Auto On/Off
        auto_off: Auto Off

    """

    def __init__(self):
        self.auto_save = ['HSAutoSaveFunction', 'Exist']
        self.auto_on_off = ['HSAutoOnOffFunction', 'Exist']
        self.auto_off = ['HSAutoOffFunction', 1]

    def change_existence(self, n):
        """機能を無しにする

        Args:
            n: なくしたい機能番号
        """
        func_table = [self.auto_save, self.auto_on_off]
        func_table[n][1] = 0

    def change_auto_off_level(self, n):
        """auto offレベル変換

        Args:
            n: 変更したいレベル
        """
        self.auto_off[1] = n


def create_function_table():
    """ 親子機機能

    親子機テストシステムに対象機能を作成

    Returns:
        機能有無つき二次元配列
    """

    human_sensor = HumanSensor()
    fan_strength = FanStrength()
    other_function = OtherFunction()
    new_fan_strength = NewFanStrength()
    louver_vt = LouverVT()
    louver_ht = LouverHT()
    func_table = [human_sensor.auto_save, human_sensor.auto_on_off,
                  human_sensor.auto_off, other_function.economic,
                  other_function.anti_freeze, other_function.central,
                  other_function.filter_sign, new_fan_strength.highhigh,
                  new_fan_strength.mediumhigh, new_fan_strength.lowlow,
                  fan_strength.auto, fan_strength.high,
                  fan_strength.quiet, louver_vt.vt_1, louver_vt.vt_2,
                  louver_vt.vt_3, louver_vt.vt_4, louver_ht.ht_1,
                  louver_ht.ht_2, louver_ht.ht_3, louver_ht.ht_4]
    return func_table
