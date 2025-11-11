'''
程式大綱：
1) 函式定義方式
2) 不定長度的函式：*引數
3) 關鍵字函式
'''

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
    

## 當函式裡有參數給定預設值時，之後的參數都必須有預設值
def pers(a, b=10, c=20):
    pass

pers(10)        # a == 10, b == 10, c == 20
pers(1,2)       # a == 1, b == 2, c == 20
pers(1,2,3)     # a == 1, b == 2, c == 3


'''
## 這樣的寫法不可以，「c 沒有預設值」
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
sumScore()                    # 0
sumScore(10,20,30,40)         # 100
sumScore(1,2)                 # 3
sumScore(1,2,3,4,5,6,7)       # 28
    
print()
print('-'*20, 'sumNumber(n)', '-'*20)
print('1~10的總和：', sumNumber(11))    # 55
print('1~50的總和：', sumNumber(51))    # 1275

print()
print('-'*20, 'personal()', '-'*20)
print()
personal('王小美', '女')                # 王小美\n、女\n、臺中市\n
print()
personal('陳小華', '男', '桃園市')       # 陳小華\n、男\n、桃園市\n
print()

personal(sex='男', name='李小龍', city='台北市')	# 關鍵字函式    # 李小龍\n、男\n、台北市\n
