'''
程式大綱：大樂透 Part3 (合併 Ex03_Lottery1_Player.py 與 Ex04_Lottery2_Computer.py)
玩家自選6個號碼
電腦開出6個號碼
及2種兌獎功能 
'''

import random   # 匯入 亂數 函式庫

com = []        # 串列：大樂透開獎號碼

## 大樂透開獎號碼 6 碼
while len(com) < 6 :
    num = random.randint(1,49)
    if com.count(num) == 0:
        com.append(num)
        

myNumber = []   # 串列：自選號碼

## 自選6個號碼
while len(myNumber) < 6 :
    n = int(input('輸入1~49之間的號碼，不要重複：'))
    
    if 1 <= n <= 49 :
    
        if myNumber.count(n) == 0 :
            myNumber.append(n)
        else:
            print('號碼已重複')
            
    else:
        print('號碼超出')
               

print('你選的號碼：',myNumber)

print('開獎號碼：',com)

## 兌獎 第一種方式：com.count(myn)
total = 0
for i in range(6):
    myn = myNumber[i]
    count = com.count(myn)
    if count > 0:
        total += 1
        
print('中獎數量：',total)


## 兌獎 第二種方式：if i in com
total = 0
for i in myNumber:
    if i in com:  # 在 if 中用 in  表示是否包含 => i 變數內容是否有在 com 裡面
        total += 1
print('中獎數量：',total)        
        




    
    











