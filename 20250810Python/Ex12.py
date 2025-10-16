device = {'light':1,'temperature':26,'door':1}

for item in device:
    print(item)
    
    if item == 'light':
        if device[item] == 0:
            print('已關燈')
        else:
            print('開燈')
            
            
            
    