from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 수창동
1 지산동
2 서호동
3 이현동
4 평리동
5 대명동
6 노원동
7 신암동
8 태전동
9 만촌동
10 호림동
11 현풍읍
12 이곡동
13 시지동
14 진천동
15 다사읍
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
