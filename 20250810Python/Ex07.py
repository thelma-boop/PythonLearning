number = [1,4,7, 20,80,40,20,10,3]

# sort 排序，預設小至大 ，原本位置會異動

number.sort()
print(number)

number.sort(reverse=True) # 由大至小排序
print(number)

num = [1,4,7, 20,80,40,20,10,3]

new_num = sorted(num) # 將排序後的結果交予 new_num ，num 本身不會變
desc_num = sorted(num,reverse=True)

print('原本：',num)
print('排序後:',new_num)
print('遞減排序後:',desc_num)
