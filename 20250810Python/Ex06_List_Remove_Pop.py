'''
程式大綱：
刪除串列中的值
list.remove(value)
list.pop()
list.pop(index)
'''

#刪除
score = [10,20,30,40,50]

score.remove(30)  # 要刪除的資料一定要有。才可以

print(score)      # [10,20,40,50]

#使用索引值
n = score.pop()   # 抓取最後一個
print(n)          # 50
print(score)      # [10,20,40]

n = score.pop(1)  # 抓取 索引為1 的值
print(n)          # 20
print(score)      # [10,40]

