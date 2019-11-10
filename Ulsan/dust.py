from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 대송동
1 성남동
2 부곡동(울산)
3 여천동(울산)
4 야음동
5 삼산동
6 도로변
7 신정동
8 덕신리
9 무거동
10 효문동
11 화산리
12 상남리
13 농소동
14 삼남면
15 약사동
16 전하동

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
