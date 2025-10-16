'''
程式大綱：建立水果倉庫
1) 未建檔的水果：新增該水果
2) 已建檔的水果：顯示水果編號
'''
fruit = []

print('工會快樂水果店')

while True:
    q = input('請輸入查詢的水果，q離開：')
    if q == 'q':
        break
    
    if fruit.count(q) > 0 :
        
        print('有找到，索引值在：',fruit.index(q))
        
        #idx = fruit.index(q)
        #print('有找到，索引值在：',idx)
                
    else:
        
        q2 = input('找不到，是否要新增(y/n):')
        if q2 == 'y':
            fruit.append(q)

        
