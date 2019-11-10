from test import *
import json

CONFIG_FILE= dust_File
CONFIG={}
village = 2 
"""
0 읍내동
1 문평동
2 문창동
3 구성동
4 노은동
5 상대동(대전)
6 대흥동1
7 성남동1
8 대성동
9 정림동
10 둔산동
11 월평동

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
