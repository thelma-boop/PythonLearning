'''
程式大綱：
1) 此處import Fun_Ex07.py
2) 比較Fun_Ex07.py 有無加上「if __name__ == '__main__':」的結果

---------------------------------------------------------------
第8~11行 可被取代為 第14行
import Fun_Ex07

Fun_Ex07.hello()
Fun_Ex07.maxValue(5,7)
'''

from Fun import hello,area,maxValue

hello()
maxValue(10,20)


'''
Fun_Ex07.py 若沒有加上「if __name__ == '__main__':」，
當Ex07_Fun.py 引用 Fun_Ex07.py 時，
執行後，亦會將 Fun_Ex07.py 本身呼叫函式之結果顯示出來
> 執行結果：
你好            ## from Fun_Ex07.py
Hello           ## from Fun_Ex07.py
30 最大         ## from Fun_Ex07.py
面積： 200      ## from Fun_Ex07.py
你好            ## from Ex07_Fun.py
Hello          ## from Ex07_Fun.py
20 最大         ## from Ex07_Fun.py
'''


'''
Fun_Ex07.py 若加上「if __name__ == '__main__':」，
當Ex07_Fun.py 引用 Fun_Ex07.py 時，
執行後，只會顯示 Ex07_Fun.py 本身呼叫函式的結果
> 執行結果：
你好            ## from Ex07_Fun.py
Hello          ## from Ex07_Fun.py
20 最大         ## from Ex07_Fun.py
'''

