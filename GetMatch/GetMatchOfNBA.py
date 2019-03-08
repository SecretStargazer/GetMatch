import requests
import pandas
import datetime
import json
import PrintResult
 
def getMatch(startDay=datetime.datetime.now().strftime("%Y-%m-%d"),endDay=datetime.datetime.now().strftime("%Y-%m-%d")):
    select_data = list()
    result_data = list()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "http://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime={0}&endTime={1}&callback=ajaxExec&_=1642571643524".format(startDay  , endDay)    
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    datas = json.loads(web_data.text[9:-1])
    try:
        for day in pandas.date_range(startDay,endDay):
            day = day.strftime('%Y-%m-%d') 
            select_data += datas['data'][day]
    except:
        return result_data
    for one in select_data:
        matchType = one['matchType'] 
        if matchType == "2":
            leftName = one['leftName']
            leftGoal = one['leftGoal']
            rightName = one['rightName']
            rightGoal = one['rightGoal']
            matchPeriod = one['matchPeriod']
            period = getPeriod(matchPeriod)
            startTime = one['startTime']
            quarter = one['quarter']
            quartertime = one['quarterTime']
            result_data.append([leftName , leftGoal , rightName, rightGoal,period, quarter, quartertime, startTime])
    return result_data

def getPeriod(matchPeriod):
    period = ""
    if matchPeriod == '0':
        period = "未开始"
    elif matchPeriod == '1':
        period = "进行中"
    elif matchPeriod == '2':
        period = "已结束"
    return period

if __name__ == "__main__":
    result_data = getMatch()
    PrintResult.printMatch(result_data)
