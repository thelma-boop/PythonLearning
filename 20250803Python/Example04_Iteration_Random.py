"""
程式大綱：
1) for 迴圈
2) while 迴圈
3) 亂數函式: random.randint(1,100)
4) 猜數字遊戲

range(初始值, 終止值, 間隔值)

range(1,10,1)	# => 1,2,3,4,5,6,7,8,9

range(1,10,2)	# => 1,3,5,7,9

range(2,10)		# => 2,3,4,5,6,7,8,9

range(5)		# => 0,1,2,3,4

range(10,1,-1)	# => 10,9,8,7,6,5,4,3,2
"""

# for i in range(5) :
#     print("第",i+1,"次")
#     print("Homework")

##-------------------------------

# print("1加到1000的總和：")
# total = 0
# 
# for i in range(1,1001) :
#     total = total + i	# => total += i
#     
# print(total)

##-------------------------------

# evenSUM = 0
# oddSUM = 0
# threeSUM = 0
# 
# for i in range(1,11) :
#     if i%2 == 0 :
#         evenSUM = evenSUM + i
#         
#     elif i%2 == 1 :
#         oddSUM = oddSUM + i
#         
#     if i%3 == 0 :
#         print(i)
#         
# print("偶數和：", evenSUM)
# print("奇數和：", oddSUM)


##-------------------------------

# for i in range(100) :
#     if i == 10 :
#         break		# 立即跳出當下的迴圈
#     
#     if i % 3 == 0 :
#         continue	# 以下迴圈的程式不做，換 下一個 i
#     
#     print(i)
#     
# print("FINISH")

##-------------------------------

"""
while 條件判斷式
    成立時才執行
"""

# i = 1
# 
# while i < 10 :
#     print(i)
#     i = i+2
#     
# print("FINISH")


##-------------------------------

# import random		# 匯入亂數的函式庫
# 
# top = 100
# bottom = 1
# guess = 0
# count = 1
# result = random.randint(1,100)		# 得到整數亂數
# 
# while guess != result :
#     
#     if guess == 0 :
#         print("請輸入",bottom,"~",top,"之間的整數")
#         guess = int(input())		# 將 字串轉為整數
#     elif guess > result :
#         top = guess
#         print("請輸入",bottom,"~",top,"之間的整數")
#         guess = int(input())		# 將 字串轉為整數
#     elif guess < result :
#         bottom = guess
#         print("請輸入",bottom,"~",top,"之間的整數")
#         guess = int(input())		# 將 字串轉為整數
#     else:
#         print("猜對了")


##-------------------------------
        
## 巢狀迴圈

# for i in range(1,10) :
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j,end="\t")
#         
#     print()
        
        
##-------------------------------

for i in range(10) :
    for j in range(20) :
        if j == 2 :
            break		# 離開 j 迴圈
        print(i,j)
        
print("FINISH")

##-------------------------------




##-------------------------------
