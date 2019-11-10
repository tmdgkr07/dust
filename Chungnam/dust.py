from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 성황동
1 백석동
2 성성동
3 성거읍
4 사곡면
5 공주
6 부여읍
7 독곶리
8 동문동
9 대산리
10 송산면
11 당진시청사
12 모종동
13 배방읍
14 도고면
15 둔포면
16 인주면
17 논산
18 파도리
19 이원면
20 태안읍
21 예산군
22 대천2동
23 주교면
24 홍성읍
25 내포
26 금산읍
27 청양읍
28 엄사면
29 서천읍
30 서면
31 장항읍

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
