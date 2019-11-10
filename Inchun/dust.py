from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 신흥
1 송림
2 구월동
3 숭의
4 석바위
5 부평역
6 부평
7 연희
8 검단
9 계산
10 고잔
11 석남
12 송해
13 동춘
14 운서
15 송현
16 논현
17 청라
18 송도
19 원당
20 길상
21 삼산
22 석모리
23 덕적도
24 백령도

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
