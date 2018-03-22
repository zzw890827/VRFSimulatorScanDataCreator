#!/usr/bin/python3

"""コントロール

本アプリファイル関係

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-19T20:47:51+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'

import csv
from controller import build_master_slave_test_system


def create_vrf_system_list(items):
    """ 親子機テスト

    親子機テストシステムを構築構築

    Args:
        items: 試験項目配列
    Returns:
        システム２次元配列
    """

    result = []
    vrf_unit_object_list = build_master_slave_test_system(items)
    for element in vrf_unit_object_list:
        row = []
        for name, value in vars(element).items():
            row.append(value)
        result.append(row)

    return result


def write_csv_file(array, file_path):
    """ CSVファイルを書き出し
    Args:
        array: 出力しようとする配列
        file_path: 出力場所
    Returns:
        CSVファイル
    Raises:
        データは存在しない場合、ValueErrorをあげる
    """
    with open(file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        if array:
            for row in array:
                writer.writerow(row)
        else:
            raise ValueError
    output_file.close()
