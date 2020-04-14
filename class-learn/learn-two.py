# -*- coding:utf-8 -*-
class learn_2():
    #类变量
    a = 1
    b = 2
    def __init__(self,a,b):
        #实例变量
        self.a = a
        self.b = b
        self.c = 1
        self.d = 2
    #类方法
    @classmethod
    def one(self,x,y):
        return x*y
    #静态方法
    @staticmethod
    def two():
        print('这是个静态方法')
        print()
    #实例方法
    def three(self,a,b):
        ab = a*b
        print(ab,self.c,self.d)
if __name__ == '__main__':
    print(learn_2.one(1,2))
    learn_2.two()
    a = 3
    b = 4
    c = 5
    d = 10
    # learn_2(a,b).three(a,b)
    learn_2(a,b).three(c,d)
