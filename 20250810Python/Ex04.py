import random

com = []

while len(com) < 6 :
    num = random.randint(1,49)
    if com.count(num) == 0:
        com.append(num)
        
print(com)        