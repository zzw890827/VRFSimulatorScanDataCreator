#!/usr/bin/python3

"""システムを構築

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-22T15:36:02+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

from model import *


def build_master_slave_test_system(items):
    """ 親子機テスト

    親子機テストシステムを構築構築

    Args:
        items: 試験項目配列
    Returns:
        システムobject配列
    """
    vrf_system = []
    function_table = create_function_table()

    for i in range(len(items)):  # 項目ループ分
        init_outer_node_adr = 65
        outer = Outdoor(i, init_outer_node_adr, i)  # 室外機を作成
        # 親機1
        vrf_system.append(outer)
        j = 0
        total = 8
        if items[i] == 2:  # 人感センサ
            total = 10
        ac_adr = 1

        while j < total:
            inner = Indoor(i, j, i, j, 0)  # 親機
            inner.function.append(function_table[items[i]])
            slave = Indoor(i, j + 1, i, j, ac_adr)
            slave.function.append(function_table[items[i]])
            slave.list_all_members()
            vrf_system.append(inner)
            vrf_system.append(slave)
            j = j + 2
            ac_adr = ac_adr + 1
    return vrf_system
