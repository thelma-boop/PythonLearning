'''
程式大綱：
1) 學生成績判斷 list.append()、len(list)
2) 對 Dictionary 做排序 sorted
'''

students = {'Peter':50,'Bill':95,'Mary':89,'Sue':56,'Eric':88}

low60 = []    # 串列：收集成績低於 60分 的學生名字

## k: 取得 字典的 KEY；v: 取得 字典的 VALUE
for k,v in students.items():
    if v < 60:
        low60.append(k)

## len(listName)：串列個數
print('不及格人數：',len(low60),'有',low60)    # 不及格人數： 2 有 ['Peter', 'Sue']


for k in sorted(students):  # 對 students 的 key 排序 (此處按「字母順序」排)
    print(k,students[k])
    ## Bill 95 
    ## Eric 88
    ## Mary 89
    ## Peter 50
    ## Sue 56

print()
print(students)             # {'Peter': 50, 'Bill': 95, 'Mary': 89, 'Sue': 56, 'Eric': 88}
print(sorted(students))     # ['Bill', 'Eric', 'Mary', 'Peter', 'Sue'] <class 'list'>

    
