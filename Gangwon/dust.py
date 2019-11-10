from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 중앙로
1 석사동
2 방산면
3 양구읍
4 중앙동(원주)
5 명륜동(강원)
6 문막읍
7 옥천동
8 천곡동
9 남양동1
10 평창읍
11 북평면
12 정선읍
13 간성읍
14 치악산
15 횡성군
16 상리
17 양양군
18 속초시(금호동)
19 철원군
20 홍천읍
21 영월읍
22 화천군
23 태백시
24 인제군
"""

def readConfig(filename):
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main():
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)
    stationName = CONFIG['list'][village]['stationName']
    pm10        = CONFIG['list'][village]['pm10Value']
    pm25        = CONFIG['list'][village]['pm25Value']
    no2         = CONFIG['list'][village]['no2Value']
    so2         = CONFIG['list'][village]['so2Value']
    co          = CONFIG['list'][village]['coValue']
    dataTime    = CONFIG['list'][village]['dataTime']
    
    print(stationName)
    print(pm10)
    print(pm25)
    print(no2)
    print(so2)
    print(co)
    print(dataTime)


if __name__ == "__main__":
    main()
