'''
程式大綱：
使用 Dictionary 製作「學生成績輸入系統」
'''

print('學生成績輸入系統')
students = {}

while True:
    name = input('學生姓名(q離開)：')
    if name == 'q':
        break

    ## 若 USER 輸入的學生姓名在 students 裡，則印出該學生姓名及成績
    if name in students:
        print(name,'分數：',students[name])

    ## 若 USER 輸入的學生姓名不在 students 裡，則新增該學生姓名及成績至 students
    else:
        score = int(input('分數：'))
        students[name] = score
        
        
print(students)        

    
