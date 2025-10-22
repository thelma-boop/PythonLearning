'''
程式大綱：大樂透 Part2
電腦隨機開出6個號碼，不重覆
'''

import random

com = []

while len(com) < 6 :
    num = random.randint(1,49)
    if com.count(num) == 0:
        com.append(num)
        

print(com)        
