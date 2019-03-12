from prettytable import PrettyTable

def printMatch(result_data):
    pt = PrettyTable()
    pt._set_field_names(('客队 客队比分 主队 主队比分 状态 节次 本节剩余时间 开赛时间').split(' '))
    for one in result_data:
        pt.add_row(one)
    print(pt)

def printRankingOfNBA(result_data,areaName):
    pt = PrettyTable()
    pt._set_field_names(('排名 球队 胜 负 胜场差 胜率 主队 客队 得分 失分 净胜').split(' '))
    area_data = result_data[areaName]
    for teamNum in area_data:
        serial = area_data[teamNum]['serial']
        teamName = area_data[teamNum]['teamName']
        wins = area_data[teamNum]['wins']
        losses = area_data[teamNum]['losses']
        games_back = area_data[teamNum]['games-back']
        wining_percentage = area_data[teamNum]['wining-percentage']
        homeWins = area_data[teamNum]['homeWins']
        homeLosses = area_data[teamNum]['homeLosses']
        awayWins = area_data[teamNum]['awayWins']
        awayLosses = area_data[teamNum]['awayLosses']
        points = area_data[teamNum]['points']
        lossPoints = area_data[teamNum]['lossPoints']
        pointsDifference = area_data[teamNum]['pointsDifference']
        pt.add_row([serial,teamName,wins,losses,games_back,wining_percentage + '%',homeWins + '-' + homeLosses,awayWins + '-' + awayLosses,points,lossPoints,pointsDifference])
    print(pt)
    pass