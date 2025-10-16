
students = [ [90,80,70,60] , [99,88,77,99] , [60,70,80]  ]
#              0  1  2  3      0  1  2  3      0  1  2    索引值
#                 0                 1             2       索引值

stu = [10,20,30,40]

print(students[2])   #[60,70,80]

print(students[1][2]) # 77


for i in students:
    print(i)
    

print()

for i in students:
    for x in i:
        print(x)


    
    

