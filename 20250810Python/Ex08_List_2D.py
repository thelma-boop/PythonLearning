'''
程式大綱：二維串列
'''

students = [ [90,80,70,60] , [99,88,77,99] , [60,70,80]  ]
#              0  1  2  3      0  1  2  3      0  1  2    索引值
#                 0                 1             2       索引值

print(students[2])        # [60,70,80]

print(students[1][2])     # 77


for i in students:
    print(i)

# [90,80,70,60]
# [99,99,77,99]
# [60,70,80]
    
print()    # 分隔線

for i in students:
    for x in i:
        print(x)

# 90
# 80
# 70
# 60
# 99
# 88
# 77
# 99
# 60
# 70
# 80


    
    


