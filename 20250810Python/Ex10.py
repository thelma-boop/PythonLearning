# dict 字典
"""
鍵key 不重複， value值 可以重複

{key:value,key1:value1}

{ 鍵:值 , 鍵2:值2 }

{ 'Tom':100 , 'John':90  }

{100:'A' , 90:'B' , 80:'C' }


"""

students = {'Peter':99,'Mary':90,'John':70,'Sue':100}

print(students['Mary'])

students['Mary'] = 92  # key 已經有，那就修改

print(students)

students['Eric'] = 95  # key 沒有。就新增

print(students)

#print(students['Bill']) 沒有 key 時，會error

print(students.get('Bill'))
print(students.get('Bill','找不到'))
print(students.get('Bill',0))
print(students.get('Eric',0))



