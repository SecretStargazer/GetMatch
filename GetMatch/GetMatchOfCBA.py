import requests
import pandas
import datetime
import json
 
def getNow():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://ziliaoku.sports.qq.com/cube/index?cubeId=43&dimId=152&params=&from=sportsdatabase&callback=reqwest_1551862436256"  
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    datas = json.loads(web_data.text[22:-1])
    select_data = list()
    round = datas['data']['cbaCurrentRound']['round']
    seasonId = datas['data']['cbaCurrentRound']['seasonId']
    return round,seasonId

def getRoundNow():
    round,seasonID = getNow()
    return round

def getSeasonIdNow():
    round,seasonId = getNow()
    return seasonId

def getMatch(round=getRoundNow(), seasonId=getSeasonIdNow()):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "https://ziliaoku.sports.qq.com/cube/index?cubeId=43&dimId=127&needArr=1&from=sportsdatabase&params=t4:{0}-10-18~{1}-05-01|t29:{2}&callback=reqwest_1551864749894".format(seasonId,str(eval(seasonId) + 1),round)   
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    datas = json.loads(web_data.text[22:-1])
    select_data = list()
    result_data = list()
    try:
        select_data += datas['data']['cbaMatch']
    except:
        return result_data
    for one in select_data:
        awayName = one['awayName']
        awayGoal = one['awayGoal']
        homeName = one['homeName']
        homeGoal = one['homeGoal']
        startTime = one['startTime']
        period = one['period']
        quarter = one['quarter']
        quartertime = one['quarterTime']
        result_data.append([awayName , awayGoal , homeName, homeGoal, period ,quarter, quartertime, startTime])
    return result_data
    