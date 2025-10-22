'''
程式大綱：大樂透 Part1
自選6個號碼(1~49)，不重覆
'''

myNumber = []

while len(myNumber) < 6 :
    n = int(input('輸入1~49之間的號碼，不要重複：'))
    
    if 1 <= n <= 49 :
    
        if myNumber.count(n) == 0 :
            myNumber.append(n)
        else:
            print('號碼已重複')
            
    else:
        print('號碼超出')
               

print('你選的號碼：',myNumber)

        

