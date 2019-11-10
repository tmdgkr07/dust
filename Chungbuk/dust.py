from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 송정동(봉명동)
1 사천동
2 문화동
3 용암동
4 복대동
5 호암동
6 칠금동
7 장락동
8 오창읍
9 산남동
10 오송읍
11 매포읍
12 청천면
13 괴산읍
14 진천읍
15 금왕
16 음성읍
17 영동읍
18 증평읍
19 보은읍
20 옥천읍

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
