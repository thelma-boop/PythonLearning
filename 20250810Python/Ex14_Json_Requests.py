'''
程式大綱：從網站(新北Youbike站點)上以 "Json" 格式讀取資料
'''

import requests  # 上網用的第三方
import json

## 新北市 Youbike 站點資訊
url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=10"

## data = requests.get(url).text    # 將網頁資料轉換為文字格式 (此行 == line13 + line15)

data = requests.get(url)            # print(type(data)) → <class 'requests.models.Response'>
data.encoding = 'utf-8'
data = data.text                    # print(type(data)) → <class 'str'>


bike = json.loads(data)             # 文字轉換為 json 格式 <class 'list'>

'''
bike[0] == {'sno': '500201001', 'sna': 'YouBike2.0_下庄市場', 'tot': '20', 'sbi': '10', 'sarea': '八里區', 'mday': '20251028104602', 'lat': '25.14678', 'lng': '121.3999', 'ar': '舊城路21號(前)', 'sareaen': 'Bali Dist', 'snaen': 'YouBike2.0_Shia Juang Market', 'aren': 'No.21, Jiucheng Rd., Bali Dist', 'bemp': '10', 'act': '1'}
bike[1] == {'sno': '500201002', 'sna': 'YouBike2.0_八里行政中心', 'tot': '20', 'sbi': '8', 'sarea': '八里區', 'mday': '20251028101702', 'lat': '25.15397', 'lng': '121.40721', 'ar': '十三行路(靠中山路二段路口西南側人行道)', 'sareaen': 'Bali Dist', 'snaen': 'YouBike2.0_Bali District Center', 'aren': 'Shisanhang Rd. & Zhongshan Rd. Intersection (Southwest)', 'bemp': '12', 'act': '1'}
bike[2] == {'sno': '500201003', 'sna': 'YouBike2.0_八里中庄市場綜合大樓', 'tot': '28', 'sbi': '10', 'sarea': '八里區', 'mday': '20251028054601', 'lat': '25.15993', 'lng': '121.41407', 'ar': '中山路一段268巷2號(對面汽車停車場)', 'sareaen': 'Bali Dist', 'snaen': 'YouBike2.0_Bali Chung Chuang Market Multi-Purpose Building', 'aren': 'No. 2, Ln. 268, Sec. 1, Zhongshan Rd., Bali Dist.', 'bemp': '18', 'act': '1'}
依此類推...
'''

print('目前不可以借的站點')
for item in bike:                      # print(type(item)) → <class 'dict'>
    
    sbi = int(item['sbi'])             # 字串 轉換為 整數
    if sbi < 10:
    
        print('站名：',item['sna'])     # 站名： YouBike2.0_八里行政中心
        print('可借：',item['sbi'])     # 可借： 8
        print('可停：',item['bemp'])    # 可停： 12
        print()





