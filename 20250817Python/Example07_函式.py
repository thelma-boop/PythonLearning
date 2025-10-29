def sumNumber(n):
    total = 0
    for i in range(n):
        total = total + i
        
    return total


## city 參數給預設值
def personal(name, sex, city='臺中市'):
    print(name)
    print(sex)
    print(city)

## 當函式裡有預設值參數時，後面都要是預設值參數
def pers(a, b=10, c=20):
    pass

pers(10)
pers(1,2)
pers(1,2,3)

## 這樣的寫法不可以，「c 沒有預設值」
'''
def pers2(a, b=10, c):
    pass
    
pers2(1,2)		# c = ?
'''

## 不定長度的函式 *score：空的串列
def sumScore(*score):
    total = 0
    for s in score:
        total = total + s
        
    print('總和：', total)
    
print('-'*20, '不定長度的函式', '-'*20)
sumScore()
sumScore(10,20,30,40)
sumScore(1,2)
sumScore(1,2,3,4,5,6,7)
    
print()
print('-'*20, 'sumNumber(n)', '-'*20)
print('1~10的總和：', sumNumber(11))
print('1~50的總和：', sumNumber(50))

print()
print('-'*20, 'personal()', '-'*20)
print()
personal('王小美', '女')
print()
personal('陳小華', '男', '桃園市')
print()
personal(sex='男', name='李小龍', city='台北市')	# 關鍵字函式