

# class Test(object):
#     def __init__(self, vall):
#         self.val0 = vall
#
#     def fun1(self):
#         print(self.val0)
#
#     def fun2(self, va12):
#         print(va12)
#
#     def fun3(self):
#
#         print(self.fun1)
#         self.fun1()
#
#
# ins = Test(123)
# ins.new_val = "I'm a new value" # 在实例中添加数据属性


# class Person(object):
#     pass
#
#
# student = Person()
# student.name = "Gavin"  # 为实例变量student绑定name属性， 类似于赋值操作
# student.score = 100     # 为其绑定score属性
# print(student.name)
# print(student.score)
# print(Person)

"""上述的方法虽然可以为类的实例变量绑定属性，但是不够方便和elegant ,
由于类 可以起到模板的作用，故在创建实例的时候，可以将我们认为必须绑定 属性 强制填写进去，
在 python中，是通过 类中通常都会使用的一个方法，即def  __init__(self) 方法，在创建实例变量的时候，
就把 name 和 score 等属性绑上去"""


# class Person(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# student = Person('Gavin', 100)  # 传入__init__方法中需要的参数，
# print(student.name)     # student是类的实例变量，通过student引入里面的一些属性与方法，比如引用类的属性name：student.name
# print(student.score)

"""注意：

1、__init__ 方法的第一个参数永远是 self ，表示创建的实例本身，因此，在 __init__ 方法的内部，
就可以把各种属性绑定到 self，因为 self 就指向创建的 实例本身

2、使用了 __init__ 方法，在创建实例的时候就不能传入 空的参数了，必须传入与 __init__ 方法匹配的参数，
但是 self 不需要传，python解释器会自己把实例变量传进去"""

# ---------------------------------------------------------------------------------------------------


# 用类的方法来实现计算器
class Person(object):
    def __init__(self, x, y, choice):
        self.x = x
        self.y = y
        self.choice = choice

    def add(self):
        """相加"""
        sum = self.x + self.y
        # sum = num1 + num2
        return sum

    def sub(self):
        """相减"""
        sub = self.x - self.y
        return sub

    def mul(self):
        """相乘"""
        mul = self.x * self.y
        return mul

    def div(self):
        """相除"""
        div = self.x / self.y
        return div

    def square(self):
        """平方根相加"""
        squr = pow(self.x, 2) + pow(self.y, 2)
        return squr

    def add_square(self):
        """相加的结果+平方根相加的结果=这个函数"""
        c = self.add() + self.square()
        return c


print("选择运算")
print("1, 相加")
print("2, 相减")
print("3, 相乘")
print("4, 相除")

choice = input("请输入你的选择(1/2/3/4):")
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

if __name__ == "__main__":
    student = Person(num1, num2, choice)
    if choice == '1':
        print(num1, "+", num2, "=", student.add())  # 调用Person类里面的方法，用这个类的实例变量就行，student.add()

    elif choice == '2':
        print(num1, "-", num2, "=", student.sub())  # 方法是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据
    elif choice == '3':
        print(num1, "*", num2, "=", student.mul())

    elif choice == '4':
        if num2 == 0:
            print("被除数不能为0")
        else:
            print(num1, "/", num2, "=", student.div())
    else:
        print("非法输入")

    # print(student.add())    # student是类的实例变量，通过student引入里面的一些属性与方法，比如引入方法student.add()
    # print(student.square())
    # print('----------我是可爱的分割线---------------')
    # print(student.add_square())


















