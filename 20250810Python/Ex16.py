students = {'Peter':50,'Bill':95,'Mary':89,'Sue':56,'Eric':88,'蘋果':30}
        #     key :value           k    v
        
#字典的取法 ， 抓 key 會得到 value
# students() => 函式
#  [] => 取值
data = [100,200,300,400]
print(data[1])

print(students['Mary'])
print('-'*50)

        
stu1 = students['Sue']  # 只有一個值
price = students['蘋果']

print(stu1)
print(price)

allstu = students.items()
print(allstu)
liststu = list(allstu) # 轉換成串列
print(liststu)
print(liststu[0])
print(liststu[0][0])
print(liststu[0][1])

#   [  ('Peter', 50)  ,  ('Bill', 95), ('Mary', 89), ('Sue', 56), ('Eric', 88), ('蘋果', 30)  ]
#      0     1           0     1      0      1      0     1
#        0                1             2               3            4            5
print(liststu[4][0])
print(liststu[4][1])
print('-'*50)


for k in students:  # 只會得到 key
     print(k)
print('-'*50)

for item in students.items():  #會得到每一組資料 (key,value)
    print(item)
    
print('-'*50)

for k,v in students.items():  #會得到每一組資料 (key,value)二個內容 ，就可以用二個變數分別來給予
    print(k)
    print(v)




