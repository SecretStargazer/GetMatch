from prettytable import PrettyTable

def printMatch(result_data):
    pt = PrettyTable()
    pt._set_field_names(('客队 客队比分 主队 主队比分 状态 节次 本节剩余时间 开赛时间').split(' '))
    for one in result_data:
        pt.add_row(one)
    print(pt)
