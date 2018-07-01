# -*- coding: utf-8 -*-
# @Time    : 2018/6/18 18:59
# @Author  : Torre
# @Email   : klyweiwei@163.com
# 可以尝试一键获取数据, 一键启动
import getSoup
import connect_dataBase
import os
import re
from bs4 import BeautifulSoup as bs

# db连接
connectDB = connect_dataBase.ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf["brazilCup"]["host"], get_conf["brazilCup"]["user"],
                     get_conf["brazilCup"]["password"], get_conf["brazilCup"]["database"], get_conf["brazilCup"]["port"])


# url = 'http://worldcup.2014.163.com/playerrank/total/attPenGoal/' # 球员总数据
# url = 'http://worldcup.2014.163.com/playerrank/avg/attPenGoal/'  # 球员场均数据
# url = 'http://worldcup.2014.163.com/teamrank/total/goals/'  # 国家队场总数据
url = 'http://worldcup.2014.163.com/teamrank/avg/goals/'  # 国家队场均数据

soup = getSoup.getSoup(url)
trs = soup.select('tbody tr')
# print(tds)
length = len(trs)
# print(length)
players = []
for tr in trs:
    # print(row)
    player = []
    # print(len(tr))
    for td in tr:
        # 数据格式化, formatSQL
        tds = '\''+str(td.string.strip())+'\''
        # print(tds)
        # player.append(str(td.string.strip()))
        # if '' in player:
        #     player.remove('')
        player.append(tds)
        if "''" in player:
            player.remove("''")
    # print(player)
    # print(tuple(player))
    # 球员排行榜
    # sql = 'insert into playertechsum(id,player,team,games,minsPlayed,goals,attPenGoal,goalAssist,ontargetScoringAtt,totalScoringAtt,totalPass,totalCross,wonCorners,totalOffside,touchBall,fouls,outfielderBlock,yellowCard,redCard) values('+\
    #       ','.join(player)+')'
    # 球员场均榜
    # sql = 'insert into playertechavg(id,player,team,games,minsPlayed,goals,attPenGoal,goalAssist,ontargetScoringAtt,totalScoringAtt,totalPass,totalCross,wonCorners,totalOffside,touchBall,fouls,outfielderBlock,yellowCard,redCard) values('+\
    #       ','.join(player)+')'
    # 国家队排行榜
    # sql = 'insert into teamtechsum(id,team,games,goals,goalsConceded,attPenGoal,goalAssist,ontargetScoringAtt,totalScoringAtt,saves,totalTackle,interception,fouls,totalOffside,totalPass,possession,yellowCard,redCard,wonCorners) values('+\
    #       ','.join(player)+')'
    # 国家队场均数据
    # sql = 'insert into teamtechavg(id,team,games,goals,goalsConceded,attPenGoal,goalAssist,ontargetScoringAtt,totalScoringAtt,saves,totalTackle,interception,fouls,totalOffside,totalPass,possession,yellowCard,redCard,wonCorners) values(' + \
    #       ','.join(player) + ')'
    # print(sql)
    # connectDB.get_fetch(conn, cur, sql)
    # players.append(player)
print('采集完毕')


# # # 数据的格式化 很重要  "'+str(dt)+'"
# resCon = connectDB.get_cols('teamtechavg', cur)
# saveConls = []
# for row in resCon:
#     col = row[0]
#     print(col)
#     # col = '"\'+str('+ str(col) +')+\'"'
#     saveConls.append(col)
#
# print(','.join(saveConls))
