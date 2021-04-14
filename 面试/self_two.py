

# class Person(object):
#     """总之，类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都相互独立、
#     互不影响；方法是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据"""
#     """类的方法和普通函数没甚区别，当然也可以使用 默认参数、可变参数和关键字参数，
#     例子如下"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def add(self, z=16):    # 设置默认变量z=16，这只是个普通的局部变量，非实例变量，如果外部传进来z=另一个值，也会优先z=16
#         sum = self.x + self.y + z
#         return sum
#
#     def square(self):
#         squr = pow(self.x, 2)+pow(self.y, 2)
#         return squr
#
#     def add_square(self, z):    # 这里是调用是传入的变量，也是个普通的局部变量，非实例变量
#         c = self.add() + self.square() + z
#         return c
#
#
# student = Person(3, 4)
# print(student.add())
# print(student.square())
# print("--------我是可爱的分割线")
# print(student.add_square(10))
# ----------------------------------------------------------


class Box(object):
    """
    self代表类的实例，而非类；self 就是 对象/实例 属性集合
    """
    def __init__(self, boxname, size, color):
        self.boxname = boxname
        self.size = size
        self.color = color  # self就是用于存储对象属性的集合，就算没有属性self也是必备的

    def open(self, myself):     # myself可以随便命名，自定义的
        print('-->用自己的myself, 打开{0}， {1}的{2}'.format(myself.color, myself.size, myself.boxname))
        print('-->用类自己的self， 打开{0}，{1}的{2}'.format(self.color, self.size, self.boxname))

    def close(self):
        print('-->关闭{0}，谢谢'.format(self.boxname))


b = Box('魔盒', '14m', '红色')
b.close()
b.open(b)   # 本来就会自动传一个self，现在传入b，就会让open多得到一个实例对象本身，print看看是什么
print(b.__dict__)   # 这里返回的就是self本身，self存储属性， 没有动作


# --------------------------------------------------------------------





"""
python 中一些特殊的实例变量：

1、私有变量(private),只有内部可以访问，外部不能访问，私有变量是在名称前以两个下划线开头，
如：__name，其实私有变量也不是完全不能被外部访问，不能直接访问是
因为python解释器对外把 __name 变量改成了 _类名__name,
所仍然可以通过 _类名__name 来访问 __name .

2、在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以，不能用__name__、__score__这样的变量名。

3、以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，
请把我视为私有变量，不要随意访问”
"""













