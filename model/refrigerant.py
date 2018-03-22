#!/usr/bin/python3

"""VRFタシステム

"""

__version__ = '1.0'
__author__ = 'Zhao Zhongwen'
__date__ = '2018-03-20T15:02:53+0900'
__license__ = 'LGPL'
__copyright__ = 'Fujitsu General Limited'
__all__ = ['Vrf', 'Outdoor', 'Indoor']


class Vrf(object):
    """VRFシステムクラス

    Attributes:
        system_version: VRFネットワーク名
        lon: USBインターフェースのインデクス番号
        lon_subnet: USBインターフェースのサブネット番号
        lon_node: USBインターフェースノードアドレス
        ver: フレームフォーマットのバージョン番号
        refrigerant_system: 冷媒系システム名称
        system_type: システムタイプ
        unit: 装置種別
        unit_name: 装置名称
        series: シリーズ種別
        ref_adr: 冷媒系アドレス
        node_adr: 冷媒系ノードアドレス
        rcg_ref_adr: リモコングループアドレス
        rcg_node_adr: リモコンノードアドレス
        ac_adr: 機器ナンバー（０：親　１～１５連番：子機）
        model: モデル
        model_name: 機種名
        indoor_unit_capacity: 室内機能力
        sub_machine_code: 子機コード
        neuron_id: 神経ID
        route: ルート
        prepare_1: 予備エリア
        prepare_2: 予備エリア
        prepare_3: 予備エリア
        prepare_4: 予備エリア
        prepare_5: 予備エリア
        prepare_6: 予備エリア
        prepare_7: 予備エリア
        prepare_8: 予備エリア
        function_1: 追加機能

    """

    def __init__(self):
        self.system_version = 'VRF System2'
        self.lon = 'LON1'
        self.lon_subnet = 200
        self.lon_node = 102
        self.ver = 'VRF2'
        self.refrigerant_system = ''
        self.system_type = ''
        self.unit = ''
        self.unit_name = ''
        self.series = 2
        self.ref_adr = -1
        self.node_adr = -1
        self.rcg_ref_adr = -1
        self.rcg_node_adr = -1
        self.ac_adr = -1
        self.model = ''
        self.model_name = ''
        self.indoor_unit_capacity = 0
        self.sub_machine_code = 'Unit'
        self.neuron_id = 'AA.BB.C2.F0.00.01'
        self.route = '/0'
        self.prepare_1 = ''
        self.prepare_2 = ''
        self.prepare_3 = ''
        self.prepare_4 = ''
        self.prepare_5 = ''
        self.prepare_6 = ''
        self.prepare_7 = ''
        self.prepare_8 = ''
        self.function = ''

    def list_all_members(self):
        """内部Attributesを表示

        """
        for name, value in vars(self).items():
            print(name + ' = ', end='')
            print(value)


class Outdoor(Vrf):
    """室外機クラス

    Attributes:
        refrigerant_system: 冷媒系システム名称
        system_type: システムタイプ
        unit: 装置種別
        unit_name: 装置名称
        ref_adr: 冷媒系アドレス
        node_adr: 冷媒系ノードアドレス
        rcg_ref_adr: リモコングループアドレス
        rcg_node_adr: リモコンノードアドレス
        ac_adr: 機器ナンバー（０：親　１～１５連番：子機）
        model: モデル
        model_name: 機種名
        
    """

    def __init__(self, ref_adr, node_adr, rcg_ref_adr):
        super(Outdoor, self).__init__()
        self.refrigerant_system = 'Refrigerant System ' + str(ref_adr)
        self.system_type = 'HeatPump'
        self.unit = 'Outdoor'
        self.unit_name = 'Outdoor Unit' + str(node_adr)
        self.ref_adr = ref_adr
        self.node_adr = node_adr
        self.rcg_ref_adr = rcg_ref_adr
        self.rcg_node_adr = node_adr
        self.ac_adr = 0
        self.model = 'Master'
        self.model_name = 'AJH040LCLAH'


class Indoor(Vrf):
    """室内機クラス

    Attributes:
        refrigerant_system: 冷媒系システム名称
        system_type: システムタイプ
        unit: 装置種別
        unit_name: 装置名称
        ref_adr: 冷媒系アドレス
        node_adr: 冷媒系ノードアドレス
        rcg_ref_adr: リモコングループアドレス
        rcg_node_adr: リモコンノードアドレス
        ac_adr: 機器ナンバー（０：親　１～１５連番：子機）
        model: モデル
        model_name: 機種名
    """

    def __init__(self, ref_adr, node_adr,
                 rcg_ref_adr, rcg_node_adr, ac_adr):
        super(Indoor, self).__init__()
        self.refrigerant_system = 'Refrigerant System ' + str(ref_adr)
        self.system_type = 'HeatPump'
        self.unit = 'Indoor'
        self.unit_name = 'Indoor Unit' + str(node_adr)
        self.ref_adr = ref_adr
        self.node_adr = node_adr
        self.rcg_ref_adr = rcg_ref_adr
        self.rcg_node_adr = rcg_node_adr
        self.ac_adr = ac_adr
        self.model = 'MiniUniversal'
        self.model_name = 'ABHA18LBTH'
