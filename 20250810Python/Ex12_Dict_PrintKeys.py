'''
程式大綱：印出 Dictionary 的 Keys
'''

device = {'light':1,'temperature':26,'door':1}

for item in device:
    print(item)        # 印出 device 的 Keys：light, temperature, door
    
    if item == 'light':
        if device[item] == 0:
            print('已關燈')
        else:
            print('開燈')
            
            
            

    
