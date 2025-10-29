from datetime import datetime
## 正規表達式 import re

current_Time = datetime.now()		# 抓取目前的時間
print(current_Time)                 # 2025-10-29 07:17:07.756948

today = datetime.today()			# 抓取目前的時間
print(today)                        # 2025-10-29 07:17:07.756979

##-----將時間轉字串 (f = 格式化)-----
date_only = today.strftime("%Y-%m-%d")		# yyyy-mm-dd (%y == yy)

print(date_only)

time_only = today.strftime("%H:%M:%S")
print(time_only)

regist_time = today.strftime("%Y/%m/%d %H:%M:%S")
print(regist_time)


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
        print(name, '在', regist, '報到')
       
## f：格式化；在字串前加 f 表示裡面會有格式化參數
print(f'共有{len(people)}人，為：{people}')
        

