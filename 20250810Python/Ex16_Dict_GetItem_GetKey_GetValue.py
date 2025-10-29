'''
程式大綱：
1) dict.items()：會取得 字典 裡，每一組 (Key, Value)
2) list(dict.items)：轉換成 串列
3) for k in students：只取得 Keys
4) for item in students.items()：取得 (Key, Value)
5) for k,v in students.items()：分別取得 Keys 與 Values
'''

students = {'Peter':50,'Bill':95,'Mary':89,'Sue':56,'Eric':88,'蘋果':30}
        #    key   :value           k    v
        
# 字典的取法 ， 抓 key 會得到 value
# students() => 函式
# [] => 取值
data = [100,200,300,400]
print(data[1])                # 200

print(students['Mary'])       # 89
print('-'*50)

        
stu1 = students['Sue']  # 只有一個值
price = students['蘋果']

print(stu1)                   # 56
print(price)                  # 30

allstu = students.items()
print(allstu)                 # dict_items([('Peter', 50), ('Bill', 95), ('Mary', 89), ('Sue', 56), ('Eric', 88), ('蘋果', 30)])
liststu = list(allstu)        # 轉換成串列
print(liststu)                # [('Peter', 50), ('Bill', 95), ('Mary', 89), ('Sue', 56), ('Eric', 88), ('蘋果', 30)]
                              #          0             1             2            3             4             5
                              #    0       1      0      1      0      1      0     1      0      1      0      1

print(liststu[0])             # ('Peter', 50)
print(liststu[0][0])          # Peter
print(liststu[0][1])          # 50

print(liststu[4][0])          # Eric
print(liststu[4][1])          # 88

print('-'*50)                 # 分隔線


for k in students:            # 只會得到 key
     print(k)                 # Peter → Bill → Mary → Sue → Eric → 蘋果

print('-'*50)                 # 分隔線

for item in students.items(): # 會得到每一組資料 (key,value)
    print(item)               # ('Peter', 50) → ('Bill', 95) → ('Mary', 89) → ('Sue', 56) → ('Eric', 88) → ('蘋果', 30)
    
print('-'*50)                 # 分隔線

for k,v in students.items():  # 會得到每一組資料 (key,value)二個內容 ，就可以用二個變數分別來給予
    print(k)                  # Peter → Bill → Mary → Sue → Eric → 蘋果
    print(v)                  # 50 → 95 → 89 → 56 → 88 → 30






