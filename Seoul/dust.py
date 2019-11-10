
import json

CONFIG_FILE="./dust_Seoul.json"
CONFIG={}
#i = 0
village = 24  

"""
0 강남구
1 강동구
2 강북구
3 강서구
4 관악구
5 광진구
6 구로구
7 금천구
8 노원구
9 도봉구
10 동대문구
11 동작구
12 마포구
13 서대문구
14 서초구
15 성동구
16 성북구
17 송파구
18 양천구
19 영등포구
20 용산구
21 은평구
22 종로구
23 중구
24 중랑구
"""

def readConfig(filename):
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main():


    i = 0    
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)
    cityName = CONFIG['list'][village]['cityName']
    pm10     = CONFIG['list'][village]['pm10Value']
    pm25     = CONFIG['list'][village]['pm25Value']
    no2      = CONFIG['list'][village]['no2Value']
    so2      = CONFIG['list'][village]['so2Value']
    co       = CONFIG['list'][village]['coValue']
    dataTime = CONFIG['list'][village]['dataTime']
  #      f = open("citynumber.txt", 'a') 
  #      print(village, cityName)
    print(pm10)
    print(pm25)
    print(no2)
    print(so2)
    print(co)
    print(dataTime)


if __name__ == "__main__":
    main()
