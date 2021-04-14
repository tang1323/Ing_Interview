
# 实例变量和类变量的区别
# class Person:
#     Country = 'china' # 类变量
#
#     def __init__(self, name):
#         self.name = name # 实例变量
#
#     def print_name(self):
#         print(self.name)
#
#
# laowang = Person('laowang')
# laoli = Person('laoli')
# laowang.print_name()    # 这是会打印实例变量，这是调用普通方法
# laoli.print_name()      # 这是会打印实例变量，这是调用普通方法
# print(laowang.Country)      # 这是打印类变量， 有实例变量会优先打印类变量，这是直接调用类变量
# print(laoli.Country)        # 这是打印类变量， 有实例变量会优先打印类变量，这是直接调用类变量


# classmethod第一个参数是cls，可以引用类变量
# staticmethod使用起来和普通函数一样，只不过放在类里去组织
# staticmethod是代码组织的需要，完全可以放到类之外
# classmethod和staticmethod的区别
class Person:

    # 这是类的属性
    Country = 'china'

    def __init__(self, name):
        self.name = name

    @classmethod
    def print_country(cls):
        print(cls.Country)

    @staticmethod
    def join_name(first_name, last_name):
        return last_name + first_name


# 这是传入的实例属性
laowang = Person('laowang')
laoli = Person('laoli')

# 为什么不输出laowang，因为@classmethod类的是不会随着方法的实例属性改变而改变
laowang.print_country()

# 为什么不输出laoli，因为@classmethod类的是不会随着方法的实例属性改变而改变
laoli.print_country()
print(laowang.Country)
print(laoli.Country)


