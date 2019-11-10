from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 중앙동(전주)
1 삼천동
2 팔복동
3 송천동
4 금암동
5 신풍동(군산)
6 소룡동
7 개정동
8 남중동
9 팔봉동
10 모현동
11 연지동
12 신태인
13 죽항동
14 고창읍
15 심원면
16 부안읍
17 새만금
18 요촌동
19 고산면
20 진안읍
21 운암면
22 임실읍
23 무주읍
24 순창읍
25 장수읍

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
