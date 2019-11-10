from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 장흥동
1 장량동
2 대도동
3 대송면
4 3공단
5 송도동
6 오천읍
7 청림동
8 성건동
9 보덕동
10 안강읍
11 외동읍
12 문당동
13 대광동
14 명륜동
15 공단동
16 원평동
17 형곡동
18 4공단
19 휴천동
20 중방동
21 상주시
22 칠곡군
23 지품면
24 화북면
25 영천시
26 안계면
27 울진군
28 석포면
29 태하리
30 울릉읍
31 대가야읍

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
