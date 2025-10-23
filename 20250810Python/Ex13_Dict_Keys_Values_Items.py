'''
程式大綱：Dictionary
1) dict.keys()：得 Dictionary 的 鍵
2) dict.values()：得 Dictionary 的 鍵之值
3) dict.items()：得 Dictionary 的 鍵+值
'''


device = {'light':1,'temperature':26,'door':1}

keys = device.keys()
values = device.values()
items = device.items()

print(keys)        # <class 'dict_keys'> dict_keys(['light', 'temperature', 'door'])
print(values)      # <class 'dict_values'> dict_values([1, 26, 1])
print(items)       # <class 'dict_items'> dict_items([('light', 1), ('temperature', 26), ('door', 1)])

for k,v in device.items():
    print(k)       # light, temperature, door
    print(v)       # 1, 26, 1
    print()
    
    
a = 10,20,30       # <class 'tuple'>
print(a)           # (10,20,30)
print(a[0])        # 10
print(a[1])        # 20
print(a[2])        # 30


q,w,e = 10,20,30
print(q)           # 10 <class 'int'>
print(w)           # 20 <class 'int'>
print(e)           # 30 <class 'int'>


