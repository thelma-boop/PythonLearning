'''
程式大綱：
串列 & 字串的「slicing(切片)」
公式：[start:end:step]
Every STEP fetches values from START to END-1
Eg. numList = [0,1,2,3,4,5,6,7,8,9]
print(numList[1:8:3]) → [1,4,7]

Eg. abcStr = 'abcdefghijk'
print(abcStr[1:8:3]) → 'beh'
'''

score = [10,80,100,98,77,99,92]

words = "abcdefghijk"

##-----從後面抓取-----
print(score[-1])        # 92
print(score[-2])        # 99


##-----串列切片-----
print(score[2:6])		# 抓取串列索引值2 ~ 5，[100,98,77,99]
print(score[3:])		# 抓取串列索引值3 ~ 最後，[98,77,99,92]
print(score[:4])		# 抓取串列索引值0 ~ 3，[10,80,100,98]


##-----一一列出字串中的字元-----
for w in words :
    print(w)            # a → b → c → d → e → f → g → h → i → j → k
    

##-----字串切片-----
print(words[:4])		# 抓取字串第0 ~ 3個字元，"a,b,c,d"
