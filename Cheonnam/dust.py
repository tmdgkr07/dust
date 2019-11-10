from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 용당동
1 부흥동
2 서강동
3 월내동
4 문수동
5 여천동(여수)
6 덕충동
7 장천동
8 연향동
9 순천만
10 호두리
11 신대
12 빛가람동
13 담양읍
14 장성읍
15 화양면
16 율촌면
17 삼일동
18 중동
19 태인동
20 진상면
21 광양읍
22 해남읍
23 나불리
24 송단리
25 화순읍
26 영광읍
27 장흥읍
28 진도읍
29 신지면
30 함평읍
31 고흥읍
32 신안군
33 무안읍
34 강진읍
35 곡성읍
36 구례읍
37 벌교읍
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
