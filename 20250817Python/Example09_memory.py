## 當兩個變數之值相同時，記憶體位址「相同」
x = 100	# 記憶體位址：2667131374928
y = 100	# 記憶體位址：2667131374928
#同 y = x	# 記憶體位址：2667131374928

print(id(x))
print(id(y))

## 當變數之值不同時，記憶體位址「重新配置」
y = 1

print(id(x))	# 記憶體位址：2667131374928
print(id(y))	# 記憶體位址：2667131371760


score = [1,2,3,4]
s = score

print('-'*50, '1')
print(id(score))
print(id(s))

s[0] = 100
print('-'*50, '2')
print(id(score))
print(id(s))
print(score)
print(s)

print('-'*50, '3')
import copy

s2 = copy.copy(s)		# 一維陣列的複製，淺複製
s2[0] = 9999
print(s)
print(s2)
print(id(s))
print(id(s2))