'''
程式大綱：
1) dict.setdefault(Key,Value)
2) dict.pop(Key)：從 字典 裡，拿走 Key 且不放回，回傳此 Key 的值
3) dict.clear()：將 字典 清空
4) 字典表達示：Dictionary Comprehension
           公式：
           。dictionary = {key: value for vars in iterable}
           。dictionary = {key: value for k:v in dict.items()}
           。dictionary = {key: value for k:v in dict.items() if condition}
           
           參考：https://www.programiz.com/python-programming/dictionary-comprehension
'''

student = {'Peter':90,
           'Bill':85}

##-----新增預設值dict.setdefault-----
student.setdefault('John')                      # 可不設定其 Value，預設為 None
student.setdefault('Mary', 60)                  # 沒有，就新增
student.setdefault('Peter', 60)                 # 已存在時，不會作任何更改
print(student)                                  # {'Peter': 90, 'Bill': 85, 'John': None, 'Mary': 60}

s = student.pop('Bill')                         # 取出不放回
print(s)                                        # Bill 的值：85
print(student)                                  # {'Peter': 90, 'John': None, 'Mary': 60}

student.clear()                                 # 整個清除
print(student)                                  # {}


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
'''
分數大於80分有：
{'Tom': 80, 'Mary': 90}
'''


print('分數小於80分有：\n', { k:v for k,v in score.items() if v < 80 })		# 字典表達式。有符合條件的結果 放回 k:v
'''
分數小於80分有：
 {'Bill': 45, 'John': 55, 'Sue': 70}
'''

print('-'*50)           # 分隔線

data = zip(score.values(), score.keys())
print(list(data))                                            # [(80, 'Tom'), (45, 'Bill'), (55, 'John'), (90, 'Mary'), (70, 'Sue')]

min_score = min(zip(score.values(),score.keys()))
print('最低：', min_score)                                    # 最低： (45, 'Bill')

max_score = max(zip(score.values(),score.keys()))
print('最高：', max_score)                                    # 最高： (90, 'Mary')

'''
以下做法也行
data = zip(score.values(), score.keys())    # 透過 zip 重組字典，使Value排在前，Key排在後
data = list(data)                           # 要將 data 轉換成 list 後，才能放入 min() 與 max() 而不會出錯
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
