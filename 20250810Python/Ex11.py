print('學生成績輸入系統')
students = {}

while True:
    name = input('學生姓名(q離開)：')
    if name == 'q':
        break
    
    if name in students:
        print(name,'分數：',students[name])
        
    else:
        score = int(input('分數：'))
        students[name] = score
        
        
print(students)        
    