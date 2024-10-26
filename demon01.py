# if __name__=='__main__':
#     print('hello')
# #注释  单行注释
# '''
# 多行注释
# '''


import keyword

#常量 python中没有常量
#一般常量用大写字母
PI=3.14

#变量规范 大小写字母、数字、下划线，但不能数字开头
a=10
_a=11
#不能为保留字(关键字)
print(keyword.kwlist)

#驼峰命名法 用在类的定义上
trainHead=1
#见名知意思
train_head=1
huo_che_tou=1
print(type(train_head))
#输出input 接受的所有的东西都是字符串类型
# age=input("请输入你的年龄：")
# print(age)
#
# print(input("请输入你的年龄："))
