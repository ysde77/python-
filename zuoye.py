# #打印 hello world  单词间用***分隔
# print('hello','word',sep='***')
# # 打印hello world,  结尾不要回车
# print('hello word',end='')
# # 打印hello world,  结尾回车两行
# print('hello word',end='\n\n')
# # 打印 * 50个
# for i in range(50):  #遍历0-49
#     print('*',end='')
#
#     '''将下列汉字使用一个print原样输出,不使用换行符
# 你好
# 我是xxx
# 我来自xx学校
# 我在校期间认真学习 刻苦coding 废寝忘食  专注技术发展
# 获得过全球最优大学生称号'''
#
# text = """你好
# 我是xxx
# 我来自xx学校
# 我在校期间认真学习 刻苦coding 废寝忘食  专注技术发展
# 获得过全球最优大学生称号"""
# print(text)
#
# #使用变量接收一个人名 然后print输出 welcome 人名
# name=input("请输入姓名：")
# print('welcome'+ ' ' +name)
#
# #八进制转十进制 7654321
# #111 110 101 100 011 010 001 => 1*8^0 +2*8 +3*8^2 +4*8^3 +5*8^4 +6*8^5 +7*8^6=2054353
# print(int('7654321',8))

s1='100'
b1=s1.isdecimal()
print(s1)
print(b1)