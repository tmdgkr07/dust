
import json

CONFIG_FILE="./dust_Seoul.json"
CONFIG={}
vliage = 2 
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
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)
    cityName = CONFIG['list'][vliage]['cityName']
    pm10     = CONFIG['list'][vliage]['pm10Value']
    pm25     = CONFIG['list'][vliage]['pm25Value']
    no2      = CONFIG['list'][vliage]['no2Value']
    so2      = CONFIG['list'][vliage]['so2Value']
    co       = CONFIG['list'][vliage]['coValue']
    dataTime = CONFIG['list'][vliage]['dataTime']
    
    print(cityName)
    print(pm10)
    print(pm25)
    print(no2)
    print(so2)
    print(co)
    print(dataTime)


if __name__ == "__main__":
    main()
