
import json

CONFIG_FILE="./dust_Gyeonggi.json"
CONFIG={}
village = 3 
"""
0 신풍동
1 인계동
2 광교동
3 영통동
4 천천동
5 경수대로(동수원)
6 고색동
7 호매실동
8 대왕판교로(백현동)
9 단대동
10 정자동
11 수내동
12 성남대로(모란역)
13 복정동
14 운중동
15 상대원동
16 의정부동
17 의정부1동
18 안양6동
19 부림동
20 호계동
21 안양2동
22 철산동
23 소하동
24 고잔동
25 원시동
26 본오동
27 원곡동
28 부곡동1
29 대부동
30 호수동
31 중앙대로(고잔동)
32 별양동
33 과천동
34 교문동
35 동구동
36 부곡3동
37 고천동
38 정왕동
39 시화산단
40 대야동
41 금곡동
42 오남읍
43 별내동
44 화도읍
45 비전동
46 안중
47 평택항
48 송북동
49 금촌동
50 운정
51 파주
52 행신동
53 식사동
54 백마로(마두역)
55 신원동
56 주엽동
57 경안동
58 김량장동
59 수지
60 기흥
61 중부대로(구갈동)
62 모현읍
63 이동읍
64 백암면
65 설성면
66 창전동
67 장호원읍
68 관인면
69 선단동
70 일동면
71 사우동
72 고촌읍
73 통진읍
74 당동
75 산본동
76 오산동
77 금암로(신장동)
78 신장동
79 남양읍
80 향남읍
81 동탄
82 우정읍
83 청계동
84 백석읍
85 고읍
86 보산동
87 봉산동
88 여주
89 연천
90 가평
91 양평
92 소사본동
93 내동
94 중2동
95 오정동
96 송내대로(중동)

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
    pm10     = CONFIG['list'][village]['pm10Value']
    pm25     = CONFIG['list'][village]['pm25Value']
    no2      = CONFIG['list'][village]['no2Value']
    so2      = CONFIG['list'][village]['so2Value']
    co       = CONFIG['list'][village]['coValue']
    dataTime = CONFIG['list'][village]['dataTime']
    
    print(stationName)
    print(pm10)
    print(pm25)
    print(no2)
    print(so2)
    print(co)
    print(dataTime)


if __name__ == "__main__":
    main()
