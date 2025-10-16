'''
程式大綱：
1) 在一串列中，修改特定索引值的內容值
2) 在一串列中，插入特定索引值的內容值 insert
3) 在一串列中，找尋索引值 index
4) 在一串列中，計算某一特定內容值的數量 count
'''
fruit = ['apple','orange','banana']
print(fruit[2])          # banana

fruit[0] = 'cherry'

print(fruit)             # ['cherry', 'orange', 'banana']

#新增資料
fruit.append('apple')

print(fruit)             # ['cherry', 'orange', 'banana', 'apple']

#插入
fruit.insert(1,'guava')

print(fruit)             # ['cherry', 'guava', 'orange', 'banana', 'apple']

#找尋索引值 (注意：要找的值一定要有。不然會出錯)

idx = fruit.index('banana')

print(idx)               # 3

#計數
count = fruit.count('banana')
print(count)             # 1





