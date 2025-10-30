'''
程式大綱：
1) datetime 函式庫
2) datetime to string：strftime()
3) Example：會議報到系統
'''

from datetime import datetime
## 正規表達式 import re

current_Time = datetime.now()		# 抓取目前的時間
print(current_Time)                 # <class 'datetime.datetime'> 2025-10-29 07:17:07.756948

today = datetime.today()			# 抓取目前的時間
print(today)                        # <class 'datetime.datetime'> 2025-10-29 07:17:07.756979

##-----將時間轉字串 (f = 格式化)-----
date_only = today.strftime("%Y-%m-%d")    # yyyy-mm-dd (%y == yy)
print(date_only)                          # "2025-10-30"

time_only = today.strftime("%H:%M:%S")
print(time_only)                          # "06:48:00"

regist_time = today.strftime("%Y/%m/%d %H:%M:%S")
print(regist_time)                        # 2025/10/30 06:48:00


##-----範例：會議報到系統-----
print()
print('-'*20, '會議報到系統', '-'*20)
print()

people = {}

name = ''

while name != 'q' :
    name = input('報到人員姓名：')

    if name == 'q' :
        break

    elif name in people :
        print(name, '已經報到過')
        
    else :
        today = datetime.today()
        regist = today.strftime("%Y/%m/%d %H:%M:%S")
        people[name] = regist
        print(name, '在', regist, '報到')        # Alice 在 2025/10/30 06:55:30 報到
       
## f：格式化；在字串前加 f 表示裡面會有格式化參數
print(f'共有{len(people)}人，為：{people}')

'''
共有5人，為：{'Alice': '2025/10/30 06:55:30', 
             'Bob': '2025/10/30 06:55:46', 
             'Catheline': '2025/10/30 06:55:57', 
             'Diego': '2025/10/30 06:56:07', 
             'Ema': '2025/10/30 06:56:19'}
'''     


