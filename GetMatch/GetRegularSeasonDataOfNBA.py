import requests
import pandas
import datetime
import json
 
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
    startPos = web_data.text.index('{')
    endPos = web_data.text.rindex('}') + 1
    datas = json.loads(web_data.text[startPos:endPos])
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
                result_data[areaName][teamNum] = one
                teamNum += 1
        except:
            result_data.pop(areaName)  #删除无用字典
            continue
    return result_data