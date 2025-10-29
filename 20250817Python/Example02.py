student = {'Peter':90,
           'Mary':70,
           'Sue':80,
           'Bill':100}

print('字典：', student)
print('人數：', len(student))

print('John 有在 student 裡嗎？', 'John' in student)		# 回傳 True / False

print('Sue 有在 student 裡嗎？', 'Sue' in student)		# 回傳 True / False

del student['Bill']		# 刪除 dict 裡的 某一元素

print('字典', student)


##-----合併：欲合併的項目數量必須一致-----
name = ['Eric', 'Carol', 'Bill']
score = [90,80,70]

item = zip(name,score)
print(list(item))
print(type(item))

item = zip(name,score)		# 合併 串列
newData = dict(item)		# 相同於 data = dict(zip(name,score))
print(newData)


## 更新 (重覆一樣的 不會更新)
student.update(newData)		# 合併 dictionary
print(student)

