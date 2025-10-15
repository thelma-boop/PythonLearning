"""
區域註解

Python 的「空格」和「TAB」是不一樣的
        『縮排』使用「TAB」
        
【判斷式結構】
if 條件 :
    成立時 執行
_____________________
if 條件 :
    成立時 執行
else:
    不成立時執行

"""


# age = 20

# if age >= 23 :
#     print("大學畢業")
#     
# print("判斷完成")

##----------------------

# if age >= 23 :
#     print("大學畢業")
# else:
#     print("還在讀書")
#     
# print("判斷完成")

##----------------------

# score = 500
# 
# if score >= 600 :
#     print("甲")
# elif score >= 500 :
#     print("乙")
# elif score >= 400 :
#     print("丙")
# elif score == 21 :
#     print("丁")
# else:
#     print("重考")

##----------------------

# account = "python@gmail.com"
# password = "12345"

# account = input("請輸入帳號: ")
# password = input("請輸入密碼: ")
# 
# if account == "python@gmail.com" and password == "1235" :
#     print("Loggin")
#     
# else:
#     print("Try again")

##----------------------

money = 1000
ticket = True

if money >= 800:
    if ticket == True:			# ==> if ticket :
        money = money * 0.9
        print("打九折")

print("價格:", money)
