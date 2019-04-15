import GetMatchOfNBA
import GetRegularSeasonDataOfNBA
import PrintResult

def test_1():
    result_data = GetMatchOfNBA.getMatch()
    PrintResult.printMatch(result_data)

def test_2():
    rd = GetRegularSeasonDataOfNBA.getRegularSeasonData()
    text = "\
    请选择区域代码\n\
    东部：east\n\
    西部：west\n\
    大西洋赛区：atlantic\n\
    中部赛区：central\n\
    东南赛区：eastsouth\n\
    西北赛区：westnorth\n\
    太平洋赛区：pacific\n\
    西南赛区：westsouth\n\
    \n\
    输入其它文字退出\
    \n\
    输入区域："
    while True:
        area = input(text)
        try:
            PrintResult.printRankingOfNBA(rd,area)
        except:
            print('输入非指定代号，退出本功能')
            break
