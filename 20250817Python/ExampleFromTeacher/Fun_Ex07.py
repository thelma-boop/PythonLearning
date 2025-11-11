'''
程式大綱：
1) 與 Ex07.py 一起看
2) __name__ & __main__
'''

##-----無參數函式-----
def hello():
    print('你好')
    print('Hello')


##-----有參數的函式-----
def maxValue(x,y):
    if x > y:
        print(x , '最大')
    else:
        print(y, '最大')
  

##-----有參數並會回傳值的函式-----
def area(w,h):
    a = w * h
    return a



##**********主程式開始**********
if __name__ == '__main__':
    hello()
    maxValue(30,12)
    s = area(10,20)
    print('面積：',s)


'''
直接執行 "Fun_Ex07.py" 時，
> 執行結果：
你好            ## from Fun.py
Hello           ## from Fun.py
30 最大         ## from Fun.py
面積： 200      ## from Fun.py
'''


'''
此處若沒有加上「if __name__ == '__main__':」，
當Ex07.py 引用 Fun.py 時，
執行後，亦會將 Fun.py 本身呼叫函式之結果顯示出來
> 執行結果：
你好            ## from Fun.py
Hello           ## from Fun.py
30 最大         ## from Fun.py
面積： 200      ## from Fun.py
你好            ## from Ex07.py
Hello          ## from Ex07.py
20 最大         ## from Ex07.py
'''


'''
此處若加上「if __name__ == '__main__':」，
當Ex07.py 引用 Fun.py 時，
執行後，只會顯示 Ex07.py 本身呼叫函式的結果
> 執行結果：
你好            ## from Ex07.py
Hello          ## from Ex07.py
20 最大         ## from Ex07.py
'''

    





    

