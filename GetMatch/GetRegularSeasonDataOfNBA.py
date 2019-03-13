import requests
import pandas
import datetime
import json
import PrintResult
 
def getRegularSeasonData():
    area_data = list()
    select_data = list()
    team_data = dict()
    result_data = dict()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://matchweb.sports.qq.com/rank/team?from=sporthp&callback=jQuery112002240396961222011_1552286565426&competitionId=100000&from=NBA_PC&_=1552286565427"  
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    datas = json.loads(web_data.text[45:-6])
    try:
        area_data += datas
    except:
        return result_data
    areaNum = 0
    for area in area_data:
        areaName = area_data[areaNum]
        areaNum += 1
        select_data = datas[area]
        result_data[areaName] = dict()
        try:
            teamNum = 0
            for one in select_data:
                result_data[areaName][teamNum] = dict()
                result_data[areaName][teamNum]['teamName'] = one['teamName'] 
                result_data[areaName][teamNum]['wins'] = one['wins']
                result_data[areaName][teamNum]['losses'] = one['losses']
                result_data[areaName][teamNum]['serial'] = one['serial']
                result_data[areaName][teamNum]['games-back'] = one['games-back']
                result_data[areaName][teamNum]['homeWins'] = one['homeWins']
                result_data[areaName][teamNum]['homeLosses'] = one['homeLosses']
                result_data[areaName][teamNum]['awayWins'] = one['awayWins']
                result_data[areaName][teamNum]['awayLosses'] = one['awayLosses']
                result_data[areaName][teamNum]['conferenceWins'] = one['conferenceWins']
                result_data[areaName][teamNum]['conferenceLosses'] = one['conferenceLosses']
                result_data[areaName][teamNum]['divisionWins'] = one['divisionWins']
                result_data[areaName][teamNum]['divisionLosses'] = one['divisionLosses']
                result_data[areaName][teamNum]['points'] = one['points']
                result_data[areaName][teamNum]['lossPoints'] = one['lossPoints']
                result_data[areaName][teamNum]['pointsDifference'] = one['pointsDifference']
                result_data[areaName][teamNum]['wining-percentage'] = one['wining-percentage']
                result_data[areaName][teamNum]['streak'] = one['streak']
                teamNum += 1
        except:
            result_data.pop(areaName)  #删除无用字典
            continue
    return result_data

if __name__ == "__main__":
    rd = getRegularSeasonData()
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
