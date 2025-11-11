'''
程式大綱：
1) math函式庫常用函式
2) 遊戲21點 (Blackjack)
'''

import math
import random

score = [10,20,30,40,50,60]

## 內建函式
# print(max(score))
# print(min(score))
# print(sum(score))
# print(round(3.14159, 2))	# 取到小數點2位，四捨五入
# print(math.floor(3.14159))	# 無條件捨去
# print(math.ceil(3.14159))	# 無條件進位



##-----應用-----
cards = []

## 產生撲克牌：撲克牌有52張，每一花色都有13張 
for i in range(4):
    for y in range(1,14):
        cards.append(y)


## 發牌
def givePoint():
    point = cards.pop(0)	# 從序列第1個開始取
    if point >= 10:
        point = 10
        
    return point	# 回傳點數


## 洗牌
def washCard(cards):
    ## 洗 200 遍
    for i in range(200):
        f = random.randint(0, len(cards)-1) # 0~51 間，隨意取一整數值
        e = random.randint(0, len(cards)-1)
        
        ## 法一：2個位置的值交換
        temp = cards[f]
        cards[f] = cards[e]
        cards[e] = temp
        
        '''
        ## 法二：only for Python
        cards[f], cards[e] = cards[e], cards[f]
        '''
        
washCard(cards)
print('-'*20, '決戰21點', '-'*20)
print()

myMoney = 100

while myMoney > 0:
    gameP = int(input('請輸入代幣：'))
    
    if gameP > myMoney:
        print('代幣不足')
        
    print()
    print()
    print('你下注代幣：', gameP)
    
    com = list()
    player = list()
    
    com.append(givePoint())
    print('莊家：？點')
    
    player.append(givePoint())
    print('玩家：', player[0], '點')

    print('-'*50)
    
    com.append(givePoint())
    print('莊家：', com[1], '點')
    
    player.append(givePoint())
    print('玩家：', player[1], '點')
    
    print('玩家總點數：', sum(player), '點')
    
    print(len(cards))
    print('-'*50)
    
    q = "y"
    i = 2
    while q == "y":
        q = input('請問玩家是否繼續(y/n)：')
        if q != 'y':
            break
        
        player.append(givePoint())
        print('玩家：', player[i], '點')
        i = i + 1
        print('玩家總點數：', sum(player), '點')
        
        if sum(player) > 21:
            print('玩家爆了')
            break
        
        elif sum(player) == 21:
            print('玩家贏了')
            break
    
    print('莊家總點數：', sum(com), '點')
    
    if sum(player) < 21:
        i = 2
        while sum(com) < sum(player):
            com.append(givePoint())
            print('莊家:', com[i], '點')
            print('莊家總點數：', sum(com), '點')
            i = i + 1
    
    ## 判斷輸贏
    if sum(player) == 21:
        myMoney = myMoney + gameP
    elif sum(player) > 21:
        myMoney = myMoney - gameP
    elif sum(com) > 21:
        myMoney = myMoney + gameP
        print('玩家贏')
    elif sum(com) >= sum(player):
        myMoney = myMoney - gameP
        print('玩家輸')
        
        
    print('目前總代幣：', myMoney)
    ans = input('還要繼續？(y/n)')
    if ans != 'y':
        break
    
    
    
    
    
    
    

    
