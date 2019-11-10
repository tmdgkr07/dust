
import json

CONFIG_FILE="./dust_Gyeonggi.json"
CONFIG={}
village = 3 
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

"""

def readConfig(filename):
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main():
    for village in range(0,100):
        global CONFIG_FILE
        global CONFIG
        CONFIG = readConfig(CONFIG_FILE)
        stationName = CONFIG['list'][village]['stationName']
        
        print(village, stationName)
""" 
    pm10     = CONFIG['list'][village]['pm10Value']
    pm25     = CONFIG['list'][village]['pm25Value']
    no2      = CONFIG['list'][village]['no2Value']
    so2      = CONFIG['list'][village]['so2Value']
    co       = CONFIG['list'][village]['coValue']
    dataTime = CONFIG['list'][village]['dataTime']
"""    
       # print(cityName)

"""    print(pm10)
    print(pm25)
    print(no2)
    print(so2)
    print(co)
    print(dataTime)
"""

if __name__ == "__main__":
    main()
