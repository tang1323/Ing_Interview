
class A:
    # 类属性
    explanation = 'this is my programs'

    # 普通方法或实例方法
    def normalMethod(self, name):
        print(self.explanation)

    # 类方法，可以访问类属性
    @classmethod
    def classMethod(cls, explanation):
        print(cls.explanation)

    # 静态方法，不可以访问类属性，直接输出传入的方法的值
    @staticmethod
    def staticMethod(explanation):
        print(explanation)


a = A()
# 这个explanation在类属性里也有，但是只有在普通方法或实例方法才会改变， 类的方法不会改变，还是类的属性
a.explanation = 'this is new'
print(a.normalMethod('explanation'))

print(a.classMethod('explanation'))
print(A.classMethod('explanation'))

print(a.staticMethod('explanatio'))
print(A.staticMethod('explanation'))
"""
实例方法隐含的参数为类实例self，
只能用类有实例调用a.normalMethod('explanation')
实例方法（普通方法）——————————————————————随着实例属性的改变而改变

而类方法隐含的参数为类本身cls。
(也就是说a.classMethod(),也能这样调用A.classMethod())
类方法（无论是类调用还是实例调用）———————————————都是类属性的值，不随实例属性的变化而变化 

静态方法无隐含参数，主要为了类实例也可以直接调用静态方法。
(也就是说a.classMethod(),也能这样调用A.classMethod())
静态方法————————————————————————————不可以访问类属性，故直接输出传入方法的值 
"""














