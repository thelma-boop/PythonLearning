fruit = ['apple','orange','banana']
print(fruit[2])

fruit[0] = 'cherry'

print(fruit)

#新增資料
fruit.append('apple')

print(fruit)

#插入
fruit.insert(1,'guava')

print(fruit)

#找尋索引值 (注意：要找的值一定要有。不然會出錯)

idx = fruit.index('banana')

print(idx)

#計數
count = fruit.count('banana')
print(count)




