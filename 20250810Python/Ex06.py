#刪除

score = [10,20,30,40,50]

score.remove(30) # 要刪除的資料一定要有。才可以

print(score)

#使用索引值
n = score.pop() # 抓取最後一個
print(n)
print(score)

n = score.pop(1) # 抓取 1 的索引值
print(n)
print(score)
