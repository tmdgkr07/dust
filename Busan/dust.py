from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 광복동
1 초량동
2 태종대
3 전포동
4 온천동
5 명장동
6 대연동
7 학장동
8 덕천동
9 청룡동
10 좌동
11 장림동
12 대저동
13 녹산동
14 연산동
15 기장읍
16 용수리
17 수정동
18 부곡동
19 광안동
20 대신동
21 덕포동
22 개금동
23 당리동
24 부산북항
25 부산신항

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
