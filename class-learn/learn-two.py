# -*- coding:utf-8 -*-
class learn_2():
    #类变量
    j = 0
    k = 2
    def __init__(self,a1,b1):
        #实例变量
        self.a = a1
        self.b = b1
        self.c = 1
        self.d = 2
        #给类的变量变值
        learn_2.j+=1
    #类方法
    @classmethod
    def one(self,j,k):
        return j*k,k+k
    #静态方法
    @staticmethod
    def two():
        print('这是个静态方法')
        print(learn_2.j)
    #实例方法
    def three(self,a2,b2):
        ab2 = a2*b2
        #下面的self.c和self.d调用实例方法
        print(ab2,self.a,self.b ,learn_2.j ,learn_2.k)
if __name__ == '__main__':
    #调用类方法
    print(learn_2.one(1,2))
    #调用静态方法
    learn_2.two()
    #赋值，调用实例方法,调用实例方法时要先给实例变量赋值
    learn_2(3,4).three(3,4)
    learn_2(3,4).three(5,10)
    #输出类变量
    li1 = learn_2(10,20)
    print(li1.three(1,3))#实例变量重新赋值后输出实例方法
    print(li1.j)
