#!/usr/bin/python3

"""VRFタシステム

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-20T15:02:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'


class Vrf(object):
    """VRFシステムクラス

    Attributes:
        system_version: タシステムタイプ
        lon: Lon番号
        lon_subnet: Lonサブネット
        lon_node: Lonノード番号
        ver: バージョン
        series: シリーズ
        ref_adr: 冷媒系アドレス
        node_adr: ノードアドレス
        rcg_ref_adr: リモコングループアドレス
        rcg_node_adr: リモコンノードアドレス
        ac_adr:
        model:
        indoor_unit_capacity:
        sub_machine_code
        neuron_id:
        route:
        model_name:
        prepare:


    """

    def __init__(self, ref_adr, node_adr, rcg_ref_adr, rcg_node_adr,
                 ac_adr, model, sub_machine_code, model_name):
        self.system_version = 'VRF System2'
        self.lon = 'LON1'
        self.lon_subnet = 200
        self.lon_node = 102
        self.ver = 'VRF2'
        self.series = 2
        self.ref_adr = ref_adr
        self.node_adr = node_adr
        self.rcg_ref_adr = rcg_ref_adr
        self.rcg_node_adr = rcg_node_adr
        self.ac_adr = ac_adr
        self.model = model
        self.indoor_unit_capacity = 0
        self.sub_machine_code = sub_machine_code
        self.neuron_id = 'AA.BB.C2.F0.00.01'
        self.route = '/0'
        self.model_name = model_name
        self.rbg_ref_adr = ''
        self.prepare = ['', '', '', '', '', '', '', '']


class VrfUnit(Vrf):
    """VRFユニットクラス

    Attributes:
        system_name: システム名称
        system_type: システムタイプ
    """

    def __init__(self, ref_adr, node_adr, rcg_ref_adr, rcg_node_adr,
                 ac_adr, model, sub_machine_code, model_name):
        super(VrfUnit, self).__init__(ref_adr, node_adr, rcg_ref_adr,
                                      rcg_node_adr, ac_adr, model,
                                      sub_machine_code, model_name)
