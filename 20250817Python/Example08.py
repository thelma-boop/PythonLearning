x = 10
y = 100

def changeX(n):
    x = n					# 區域變數
    print('changeX=', x)


## 函式內若無定義區域變數，此函式會向外找；若外部沒有定義，就會出錯
def circle():
    area = x * x * 3.14
    print('圓面積：', area)
    

## 定義 global 時，就可以改變外部的定義
def changeY(n):
    global y				# 全域變數
    
    y = n
    print('changeY=', y)


print('x=', x)
changeX(100)
print('x=', x)

circle()

print()
print('Y=', y)
changeY(199)
print('Y=', y)