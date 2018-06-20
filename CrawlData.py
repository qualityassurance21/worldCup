# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 22:55
# @Author  : Torre
# @Email   : klyweiwei@163.com

# 爬取世界杯比赛结果, 以一定的格式输出, 保存在数据库中

from bs4 import BeautifulSoup as bs
import getSoup
import os
import re
import json
import requests
import datetime
import time
import connect_dataBase


# db连接
connectDB = connect_dataBase.ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf["worldCup"]["host"], get_conf["worldCup"]["user"],
                     get_conf["worldCup"]["password"], get_conf["worldCup"]["database"], get_conf["worldCup"]["port"])


url = 'http://api.sports.163.com/api/football/v1/2018/1002/16/groupInfo/groupby?groupType=groupName'
urlPlayer = 'http://api.sports.163.com/api/football/v1/2018/1002/16/playerTech/getList'
urlTeam = 'http://api.sports.163.com/api/football/v1/2018/1002/16/teamTech/getList'
# soup = getSoup.getSoup(url)
# soup = str(soup)
# a ='123-2638-3627 home homepages # $这是注释'
# re = re.compile(r'\bh\S*?e\b')
# home = re.findall(a)
# re = re.compile(r'"linkPreview":"(.+?)",')
# home = re.findall(soup)
# print(type(soup))
response = requests.get(urlTeam)
response.raise_for_status()
res = response.text
# print(type(res))
# res = json.dumps(res)
jsonRes = json.loads(res)
# print(jsonRes['data'])
jsonRes = jsonRes['data']
# print(len(jsonRes))
# print(type(jsonRes))
# groupList = ['A','B','C','D','E','F','G','H']
# jsonRes = jsonRes[groupList[1]]
# print(jsonRes)

# 小组赛赛程表
# for i in range(0, len(groupList)):
#     groupObj = jsonRes[groupList[i]]['scheduleList']
#     # print(groupRes)
#     loadGroup = []
#     for ii in range(0, len(groupObj)):
#         groupRes = groupObj[ii]
#         orderId = groupRes['orderId']
#         date = groupRes['date']
#         date = str(date)
#         date = date[0:10]
#         time_local = time.localtime(int(date))
#         # 转换成新的时间格式(2016-05-05 20:28:54)
#         dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#         groupName = groupRes['groupName']
#         roundType = groupRes['roundType']
#         home = groupRes['home']
#         homeScore = str(groupRes['homeScore']).strip()
#         away = groupRes['away']
#         awayScore = str(groupRes['awayScore']).strip()
#         result = (homeScore,awayScore)
#         result = ':'.join(result)
#         sql = 'insert into TeamRes(id,Mdate,groupName,roundType,home,away,res) ' \
#               'values("'+str(orderId)+'", "'+str(dt)+'", "'+str(groupName)+'", "'+str(roundType)+'", "'+str(home)+'","'+str(away)+'","'+str(result)+'")'
#         connectDB.get_fetch(conn, cur,sql)
#         # groupDate = tuple(orderId,date, groupName,roundType,home,away,result)
#         # # print(groupDate)
#         # loadGroup = loadGroup.append(','.join(groupDate))
#         # print(loadGroup)
#         # print(orderId,date, groupName,roundType,home,away,result)
#         print(sql)

# 球员数据: 场均和总数据
# iiii = 0
# for playerTec in jsonRes:
#     playerTecJson = jsonRes[playerTec]
#     print(len(playerTecJson))
#     # print(playerTecJson)
#     tablePlayer = ['playertechavg', 'playertechsum']
#     for iii in range(0, len(playerTecJson)):
#         playerJson = playerTecJson[iii]
#         player = playerJson['player']
#         # print(player)
#         team = playerJson['team']
#         games = playerJson['games']
#         minsPlayed = playerJson['minsPlayed']
#         goals = playerJson['goals']
#         goalAssist = playerJson['goalAssist']
#         totalScoringAtt = playerJson['totalScoringAtt']
#         ontargetScoringAtt = playerJson['ontargetScoringAtt']
#         totalOffside = playerJson['totalOffside']
#         yellowCard = playerJson['yellowCard']
#         redCard = playerJson['redCard']
#         totalPass = playerJson['totalPass']
#         totalTackle = playerJson['totalTackle']
#         fouls = playerJson['fouls']
#         wasFouled = playerJson['wasFouled']
#         outfielderBlock = playerJson['outfielderBlock']
#         totalCross = playerJson['totalCross']
#         interception = playerJson['interception']
#         saves = playerJson['saves']
#         penaltySave = playerJson['penaltySave']
#         attPenGoal =playerJson['attPenGoal']
#         if iiii == 0:
#             sqlPlayer = 'insert into playertechavg(player,team,games,minsPlayed,goals,goalAssist,totalScoringAtt,ontargetScoringAtt,totalOffside,yellowCard,redCard,totalPass,totalTackle,fouls,wasFouled,outfielderBlock,totalCross,interception,saves,penaltySave,attPenGoal) ' \
#                                                       'values("'+str(player)+'","'+str(team)+'","'+str(games)+'","'+str(minsPlayed)+'","'+str(goals)+'","'+str(goalAssist)+'","'+str(totalScoringAtt)+'","'+str(ontargetScoringAtt)+'","'+str(totalOffside)+'","'+str(yellowCard)+'","'+str(redCard)+'","'+str(totalPass)+'","'+str(totalTackle)+'","'+str(fouls)+'","'+str(wasFouled)+'","'+str(outfielderBlock)+'","'+str(totalCross)+'","'+str(interception)+'","'+str(saves)+'","'+str(penaltySave)+'","'+str(attPenGoal)+'")'
#             print(sqlPlayer)
#             connectDB.get_fetch(conn, cur,sqlPlayer)
#         else:
#             sqlPlayer = 'insert into playertechsum(player,team,games,minsPlayed,goals,goalAssist,totalScoringAtt,ontargetScoringAtt,totalOffside,yellowCard,redCard,totalPass,totalTackle,fouls,wasFouled,outfielderBlock,totalCross,interception,saves,penaltySave,attPenGoal) ' \
#                         'values("' + str(player) + '","' + str(team) + '","' + str(games) + '","' + str(
#                 minsPlayed) + '","' + str(goals) + '","' + str(goalAssist) + '","' + str(totalScoringAtt) + '","' + str(
#                 ontargetScoringAtt) + '","' + str(totalOffside) + '","' + str(yellowCard) + '","' + str(
#                 redCard) + '","' + str(totalPass) + '","' + str(totalTackle) + '","' + str(fouls) + '","' + str(
#                 wasFouled) + '","' + str(outfielderBlock) + '","' + str(totalCross) + '","' + str(
#                 interception) + '","' + str(saves) + '","' + str(penaltySave) + '","' + str(attPenGoal) + '")'
#             print(sqlPlayer)
#             connectDB.get_fetch(conn, cur, sqlPlayer)
#     iiii +=1


# 国家队之间的数据
iiii = 0
for teamTec in jsonRes:
    teamTecJson = jsonRes[teamTec]
    print(len(teamTecJson))
    # print(playerTecJson)
    # tablePlayer = ['playertechavg', 'playertechsum']
    for iii in range(0, len(teamTecJson)):
        playerJson = teamTecJson[iii]
        # player = playerJson['player']
        # print(player)
        team = playerJson['team']
        games = playerJson['games']
        # minsPlayed = playerJson['minsPlayed']
        goals = playerJson['goals']
        goalsConceded = playerJson['goalsConceded']
        goalAssist = playerJson['goalAssist']
        totalScoringAtt = playerJson['totalScoringAtt']
        ontargetScoringAtt = playerJson['ontargetScoringAtt']
        possession = playerJson['possession']
        totalOffside = playerJson['totalOffside']
        yellowCard = playerJson['yellowCard']
        redCard = playerJson['redCard']
        totalPass = playerJson['totalPass']
        totalTackle = playerJson['totalTackle']
        fouls = playerJson['fouls']
        wasFouled = playerJson['wasFouled']
        outfielderBlock = playerJson['outfielderBlock']
        totalCross = playerJson['totalCross']
        interception = playerJson['interception']
        saves = playerJson['saves']
        penaltySave = playerJson['penaltySave']
        attPenGoal =playerJson['attPenGoal']
        wonCorners = playerJson['wonCorners']
        if iiii == 0:
            sqlPlayer = 'insert into teamtechavg(team,games,possession,goals,goalsConceded,goalAssist,totalScoringAtt,ontargetScoringAtt,totalOffside,yellowCard,redCard,totalPass,totalTackle,fouls,wasFouled,outfielderBlock,totalCross,interception,saves,penaltySave,attPenGoal,wonCorners) ' \
                                                      'values("'+str(team)+'","'+str(games)+'","'+str(possession)+'","'+str(goals)+'","'+str(goalsConceded)+'","'+str(goalAssist)+'","'+str(totalScoringAtt)+'","'+str(ontargetScoringAtt)+'","'+str(totalOffside)+'","'+str(yellowCard)+'","'+str(redCard)+'","'+str(totalPass)+'","'+str(totalTackle)+'","'+str(fouls)+'","'+str(wasFouled)+'","'+str(outfielderBlock)+'","'+str(totalCross)+'","'+str(interception)+'","'+str(saves)+'","'+str(penaltySave)+'","'+str(attPenGoal)+'","'+str(wonCorners)+'")'
            print(sqlPlayer)
            connectDB.get_fetch(conn, cur,sqlPlayer)
        else:
            sqlPlayer = 'insert into teamtechsum(team,games,possession,goals,goalsConceded,goalAssist,totalScoringAtt,ontargetScoringAtt,totalOffside,yellowCard,redCard,totalPass,totalTackle,fouls,wasFouled,outfielderBlock,totalCross,interception,saves,penaltySave,attPenGoal,wonCorners) ' \
                        'values("'+str(team)+'","'+str(games)+'","'+str(possession)+'","'+str(goals)+'","'+str(goalsConceded)+'","'+str(goalAssist)+'","'+str(totalScoringAtt)+'","'+str(ontargetScoringAtt)+'","'+str(totalOffside)+'","'+str(yellowCard)+'","'+str(redCard)+'","'+str(totalPass)+'","'+str(totalTackle)+'","'+str(fouls)+'","'+str(wasFouled)+'","'+str(outfielderBlock)+'","'+str(totalCross)+'","'+str(interception)+'","'+str(saves)+'","'+str(penaltySave)+'","'+str(attPenGoal)+'","'+str(wonCorners)+'")'
            print(sqlPlayer)
            connectDB.get_fetch(conn, cur, sqlPlayer)
    iiii +=1

# # 数据的格式化 很重要  "'+str(dt)+'"
# resCon = connectDB.get_cols('teamtechavg', cur)
#
# saveConls = []
#
# for row in resCon:
#     col = row[0]
#     print(col)
#     col = '"\'+str('+ str(col) +')+\'"'
#     saveConls.append(col)
#
# print(','.join(saveConls))









