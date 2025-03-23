# eval函数；Python中的内置函数
# 用于去掉字符串最外侧的引号，并按照Python语句执行去掉引号后的字符串
# 语法格式：变量 = eval(字符串)
s = "3.14 + 3"
print(s)
print(type(s))
x = eval(s)  # 去掉字符串s中左右的引号，进行加法运算
print(x)
print(type(x))

hello = "你好"
print(eval("hello"))  # 去掉引号就是一个变量hello，输出为你好
print("北京欢迎你")
# print(eval("北京欢迎你"))  # 报错，去掉左右引号就是一个变量

age1 = input("年龄；")
print(age1, type(age1))  # str类型

# eval()函数经常与input()函数一起使用，用来获取用户输入的数值
age2 = eval(input("年龄："))  # 将字符串类型转换为int类型
print(age2, type(age2))  # int类型

high = eval(input("高度:"))
print(high, type(high))

