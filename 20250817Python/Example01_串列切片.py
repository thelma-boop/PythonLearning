score = [10,80,100,98,77,99,92]

words = "abcdefghijk"

##-----從後面抓取-----
print(score[-1])
print(score[-2])


##-----串列切片-----
print(score[2:6])		# 抓取串列索引值2 ~ 5
print(score[3:])		# 抓取串列索引值3 ~ 最後
print(score[:4])		# 抓取串列索引值0 ~ 3


##-----一一列出字串中的字元-----
for w in words :
    print(w)
    

##-----字串切片-----
print(words[:4])		# 抓取字串第0~3個字元