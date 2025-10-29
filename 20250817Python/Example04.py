student = {'Peter':90,
           'Bill':85}

##-----新增預設值dict.setdefault-----
student.setdefault('John')			# 可不設定其 Value
student.setdefault('Mary', 60)
student.setdefault('Peter', 60)		# 已存在時，不會作任何更改
print(student)

s = student.pop('Bill')				# 取出不放回
print(s)
print(student)

student.clear()						# 整個清除
print(student)


##-----應用-----

print()
print('-'*20, '應用範例', '-'*20)
print()

score = {'Tom':80,
         'Bill':45,
         'John':55,
         'Mary':90,
         'Sue':70}

print('分數大於80分有：\n', { k:v for k,v in score.items() if v >= 80 })		# 字典表達式。有符合條件的結果 放回 k:v
print('分數小於60分有：\n', { k:v for k,v in score.items() if v < 80 })		# 字典表達式。有符合條件的結果 放回 k:v

data = zip(score.values(), score.keys())
print(list(data))

min_score = min(zip(score.values(),score.keys()))
print('最低：', min_score)

max_score = max(zip(score.values(),score.keys()))
print('最高：', max_score)

'''
以下做法也行
data = zip(score.values(), score.keys())    # 透過 zip 重組字典，使Value排在前，Key排在後
data = list(data)							# 要將 data 轉換成 list 後，才能放入 min() 與 max() 而不會出錯
min_score = min(data)
max_score = max(data)
print(min_score)
print(max_score)

'''



##-----進階-----
'''
print('-'*20, 'lambda', '-'*20)
print('遞增排序')
asc_score = sorted(score.items(), key = lambda item:item[1])
print(asc_score)

print()

print('遞減排序')
desc_score = sorted(score.items(), key = lambda item:item[1], reverse = True)
print(desc_score)
'''