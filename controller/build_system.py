#!/usr/bin/python3

"""システムを構築

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-22T15:36:02+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from model import ExistTestFunction
from model.refrigerant import *


def build_master_slave_test_system(items):
    """ 親子機テスト

    親子機テストシステムを構築構築

    Args:
        items: 試験項目配列
    Returns:
        システムobject配列
    """
    vrf_system = []
    exist_test_function = ExistTestFunction()

    for i in range(len(items)):  # 項目ループ分
        init_outer_node_adr = 65
        outer = Outdoor(i, init_outer_node_adr, i)  # 室外機を作成
        # 親機1
        vrf_system.append(outer)
        j = 0
        total = 8
        ac_adr = 1
        if items[i] == 2:  # 人感センサ
            total = 10
            while j < total:
                inner = Indoor(i, j, i, j, 0)  # 親機
                slave = Indoor(i, j + 1, i, j, ac_adr)  # 子機
                slave.list_all_members()
                vrf_system.append(inner)
                vrf_system.append(slave)
                j = j + 2
                ac_adr = ac_adr + 1
        else:
            while j < total:
                inner = Indoor(i, j, i, j, 0)  # 親機
                slave = Indoor(i, j + 1, i, j, ac_adr)  # 子機
                if j == 0:
                    exist_test_function.change_existence(
                        items[i])  # ありあり
                    inner.function = exist_test_function.get_function(
                        items[i])
                    slave.function = exist_test_function.get_function(
                        items[i])
                if j == 2:
                    exist_test_function.change_existence(
                        items[i])  # あり
                    inner.function = exist_test_function.get_function(
                        items[i])
                    exist_test_function.change_none(items[i])  # なし
                    slave.function = exist_test_function.get_function(
                        items[i])
                if j == 4:
                    exist_test_function.change_none(items[i])  # なし
                    inner.function = exist_test_function.get_function(
                        items[i])
                    exist_test_function.change_existence(
                        items[i])  # あり
                    slave.function = exist_test_function.get_function(
                        items[i])
                if j == 6:
                    exist_test_function.change_none(items[i])  # なし
                    inner.function = exist_test_function.get_function(
                        items[i])
                    slave.function = exist_test_function.get_function(
                        items[i])
                vrf_system.append(inner)
                vrf_system.append(slave)
                j = j + 2
    return vrf_system
