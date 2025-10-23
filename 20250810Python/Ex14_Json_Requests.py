'''
程式大綱：從網站上以 "Json" 格式讀取資料
'''

import requests  # 上網用的第三方
import json

## 新北市 Youbike 站點資訊
url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=10"

## data = requests.get(url).text    # 將網頁資料轉換為文字格式 (此行 == line13 + line15)

data = requests.get(url)
data.encoding = 'utf-8'
data = data.text


bike = json.loads(data)             # 文字轉換為 json 格式

print('目前不可以借的站點')
for item in bike:
    
    sbi = int(item['sbi']) # 轉換為整數
    if sbi == 0:
    
        print('站名：',item['sna'])
        print('可借：',item['sbi'])
        print('可停：',item['bemp'])
        print()




