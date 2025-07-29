from DbPython import *
from typing import List, Tuple

def make_nodeinfo(
    node_id: int,
    x: float,
    y: float,
    z: float,
    is_master: bool,
    is_rgd: bool,
    eq_symb: List[bool]
) -> NodeInfo:
    """
    快速构造一个 NodeInfo 对象

    参数：
    - node_id: 节点编号
    - x, y, z: 坐标
    - is_master: 是否为主节点
    - is_rgd: 是否刚体连接
    - eq_symb: 长度为6的布尔列表，表示等值连接标志

    返回：
    - NodeInfo 实例
    """
    node = NodeInfo()
    node.NodeID = node_id
    node.location = [x, y, z]
    node.isMaster = is_master
    node.isRGD = is_rgd
    node.EqSymb = eq_symb
    return node



# 1. 创建计算器
calc = BridgeCalculator()

# 2. 材料（ID=1\2）
mat_1 = Material()
mat_1.ID = 1
mat_1.E = 300000
mat_1.Prxy = 0.2
mat_1.G = 125000
mat_1.Denstiy = 2000
mat_1.alpha = 1e-05
mat_1.Isconc = False
mat_1.fcuk = 0

mat_2 = Material()
mat_2.ID = 2
mat_2.E = 1950000
mat_2.Prxy = 0.2
mat_2.G = 812500
mat_2.Denstiy = 2500
mat_2.alpha = 1e-05
mat_2.Isconc = False
mat_2.fcuk = 0
calc.set_mats({1: mat_1,2: mat_2})

n_1 = make_nodeinfo(
    node_id=2,
    x=-15.0, y=-1, z=-1.0,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_2 = make_nodeinfo(
    node_id = 21,
    x=-9, y=-1, z=-1.0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_3 = make_nodeinfo(
    node_id = 34,
    x=-9, y=0, z=-1.0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_4 = make_nodeinfo(
    node_id = 4,
    x=-15, y=0, z=-1.0,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_5 = make_nodeinfo(
    node_id = 92,
    x= -15, y= -1, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_6 = make_nodeinfo(
    node_id = 102,
    x= -9, y= -1, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_7 = make_nodeinfo(
    node_id = 150,
    x= -9, y= 0, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_8 = make_nodeinfo(
    node_id = 139,
    x= -15, y= 0, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_9 = make_nodeinfo(
    node_id = 5,
    x= -15, y= -0.5, z= -1,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_10 = make_nodeinfo(
    node_id = 20,
    x= -12, y= -1, z= -1,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_11 = make_nodeinfo(
    node_id = 29,
    x= -9, y= -0.5, z= -1,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_12 = make_nodeinfo(
    node_id = 33,
    x= -12, y= 0, z= -1,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_13 = make_nodeinfo(
    node_id = 137,
    x= -15, y= -0.5, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_14 = make_nodeinfo(
    node_id = 101,
    x= -12, y= -1, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_15 = make_nodeinfo(
    node_id = 148,
    x= -9, y= -0.5, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_16 = make_nodeinfo(
    node_id = 147,
    x= -12, y= 0, z= 0,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_17 = make_nodeinfo(
    node_id = 93,
    x= -15, y= -1, z= -0.5,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)
n_18 = make_nodeinfo(
    node_id = 110,
    x= -9, y= -1, z= -0.5,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_19 = make_nodeinfo(
    node_id = 149,
    x= -9, y= 0, z= -0.5,
    is_master=True,
    is_rgd=True,
    eq_symb=[False, False, False, False, False, False]
)
n_20 = make_nodeinfo(
    node_id = 140,
    x= -15, y= 0, z= -0.5,
    is_master=True,
    is_rgd=True,
    eq_symb=[True, True, True, False, False, False]
)

elme_1 = CDBSolid95(1,[
    n_1, n_2, n_3, n_4, n_5,
    n_6, n_7, n_8, n_9, n_10,
    n_11, n_12, n_13, n_14, n_15,
    n_16, n_17, n_18, n_19, n_20
],300000.0,0.2,2549.0)

calc.add_element(1,elme_1)

elem_prop = Eleprop()
elem_prop.EleID = 1
elem_prop.CoeffWt = 1.0
elem_prop.t0 = 28
elem_prop.ts = 3
elem_prop.h = 0.001
elem_prop.alpha = 1e-05
elem_prop.Isconc = False
elem_prop.fcuk = 0
calc.set_eleprop({1: elem_prop})

# # 7. 阶段（ID=1）→ 激活 EleID=1 和 SecID=100
stg = StageInfo()
stg.stageID = 1
stg.duration = 10
stg.avertemp = 20.0
stg.elevatedtemp = 5.0
stg.reductiontemp = 2.0
stg.eleIDs_add = {1}
calc.set_stginfo({1: stg})

# # 8. 控制信息
ctl = ControlInfo()
ctl.active_dof = [True]*6
ctl.RH = 60
ctl.aframe = [0.0, 0.0, 1.0]
ctl.GaussPT_size = 8
ctl.cal_prep = False
ctl.Cal_Creep = False
ctl.Cal_Shk = False
ctl.cal_Temp = False
ctl.bCabAdjust = False
calc.set_controlinfo(ctl)

val = PhyVal_liveLd(NODE_DISP, [2, 4], False)

# 构造一个 loadingpair
pair = loadingpair()
pair.mainLoad = val
pair.Loads_Associated = [val]

# 填充 GeMvLdAnl_new
case = GeMvLdAnl_new()
case.Name = '活载计算1'
case.pLoadingGrps = [[pair]]
case.infsurfDbdir = 'D:/test_output/load'
case.ParallelNum = 4

calc.m_IsCalMvLd_new = True
calc.m_MvLds = [case]

# 9. 执行计算
print("run 之前")
ok = calc.run()
print("run 完成")
print("计算是否成功：", ok)

# 10. 导出结果
calc.show_result('D:/test_output/res')
calc.show_movld_result('D:/test_output/mov_res')
