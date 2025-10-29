'''
程式大綱：
1) 字典的長度：len(dict)
2) 字典的刪除：del dict[key]
3) in/not in：成員運算符，用於檢查某個元素是否存在於一個序列或可迭代物件中
4) 串列的合併：zip(list1,list2)
5) 用 zip 合併2個串列的結果，用 dict() 轉換為 字典
6) 字典的合併與更新：dict1.update(dict2)，合併2個字典，當2個Key相同時，更新此Key的Value；當2個Key不同時，新增dict2的Keys & Values到dict1中
'''

student = {'Peter':90,
           'Mary':70,
           'Sue':80,
           'Bill':100}

print('字典：', student)           # 字典： {'Peter': 90, 'Mary': 70, 'Sue': 80, 'Bill': 100}
print('人數：', len(student))      # 人數： 4

print('John 有在 student 裡嗎？', 'John' in student)		# 回傳 True / False，"John 有在 student 裡嗎？ False"
print('Sue 有在 student 裡嗎？', 'Sue' in student)		# 回傳 True / False，"Sue 有在 student 裡嗎？ False"

del student['Bill']		 # 刪除 dict 裡的 某一元素

print('字典：', student)           # 字典： {'Peter': 90, 'Mary': 70, 'Sue': 80}

print('-'*50)                     # 分隔線


##-----合併：欲合併的項目數量必須一致-----
name = ['Eric', 'Carol', 'Bill']
score = [90,80,70]

item = zip(name,score)      # 兩個串列合併
print(list(item))           # [('Eric', 90), ('Carol', 80), ('Bill', 70)]
print(type(item))           # <class 'zip'>

item = zip(name,score)      # 兩個串列合併
newData = dict(item)        # 相同於 data = dict(zip(name,score))
print(newData)              # {'Eric': 90, 'Carol': 80, 'Bill': 70}
print(type(newData))        # <class 'dict'>

print('-'*50)               # 分隔線



##-----更新：重覆一樣的 不會更新-----
newScore = {'Peter':100,
           'Ema':95,
           'Febu':75}

student.update(newScore)    # 合併 dictionary
print(student)              # {'Peter': 100, 'Mary': 70, 'Sue': 80, 'Ema': 95, 'Febu': 75}
