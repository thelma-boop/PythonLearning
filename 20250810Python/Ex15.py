students = {'Peter':50,'Bill':95,'Mary':89,'Sue':56,'Eric':88}

low60 = []

for k,v in students.items():
    if v < 60:
        low60.append(k)
        
print('不及格人數：',len(low60),'有',low60)


for k in sorted(students):  # 對 key 排序
    print(k,students[k])
    