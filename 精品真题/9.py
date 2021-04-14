
# ls = [3.5, "Python", [10, "LIST"], 3.6]
# print(ls[2][-1][1])

# a = 4.2e-1
# b = 1.3e2
# print(a+b)


# for s in "abc":
#     for i in range(3):
#         print(s, end="")
#         if s == "c":
#             break



# def change(a, b):
#     a = 10
#     b += a
#     return a, b
# a = 4
# b = 5
#
# print(change(a, b))



# import turtle
# for i in range(4):
#     turtle.circle(-90, 90)
#     turtle.right(180)
# turtle.done()

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i) == True:
        ls.remove(i)
print(len(ls))





