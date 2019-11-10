from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 회원동
1 봉암동
2 상봉동
3 대안동
4 상대동
5 명서동
6 웅남동
7 성주동
8 용지동
9 반송로
10 사파동
11 경화동
12 월영동
13 하동읍
14 동상동
15 삼방동
16 장유동
17 진영읍
18 저구리
19 아주동
20 사천읍
21 대산면
22 북부동
23 웅상읍
24 내일동
25 무전동
26 고성읍
27 거창읍
28 가야읍
29 함양읍
30 남해읍
31 산청읍
32 남상면
33 의령읍
34 창녕읍
35 합천읍
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
