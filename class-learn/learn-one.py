# -*- coding:utf-8 -*-
class learn():
    age = 0
    name = 'xx'
    def __init__(self,age,name):
        self.age = age
        self.name = name
        print()
i = learn(5,'xiaoming')
#实例变量输出
print(i.name,i.age)
#类变量输出
print(learn.name,learn.age)


