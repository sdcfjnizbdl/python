# 语法结构x=input('提示内容')
# 无论输入的数据是什么，x的数据类型都是字符串类型
name = input('请输入您的姓名：')
print('我的姓名是：' + name)  # name是字符串类型，所以可以用加号连接两个字符串
num = input('您的幸运数字是：')
print('我的幸运数字是：' + num)
num = int(num)  # 使用内置函数int将num装换为整型
# print('我的幸运数字为；' + num)  # num为整型，报错
print('我的幸运数字为；',num)   # 使用逗号在同一行输出，使用逗号会空一格
