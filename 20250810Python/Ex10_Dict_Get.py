"""
程式大綱：字典 Dictionary
1) 鍵key 不重複， value值 可以重複

2) Format
  {key:value,key1:value1}
  { 鍵:值 , 鍵2:值2 }
  {'Tom':100 , 'John':90}
  {100:'A' , 90:'B' , 80:'C' }

3) dict.get(Key)：取得某Key的值；若無此Key時，可設定回傳值(預設為 None)，故不會使程式出錯
"""

students = {'Peter':99,'Mary':90,'John':70,'Sue':100}

print(students['Mary'])  # 90

students['Mary'] = 92    # key 已經有，那就修改

print(students)          # {'Peter': 99, 'Mary': 92, 'John': 70, 'Sue': 100}

students['Eric'] = 95    # key 沒有。就新增

print(students)          # {'Peter': 99, 'Mary': 92, 'John': 70, 'Sue': 100, 'Eric': 95}

# print(students['Bill']) 沒有 key 時，會error

print(students.get('Bill'))              # None
print(students.get('Bill','Not Found'))  # "Not Found"
print(students.get('Bill',0))            # 0
print(students.get('Eric',0))            # 95




