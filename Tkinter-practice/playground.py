# Positional args

# def add(*args):
#     return sum(args)

# Another method for add()
# def add(*args):
#     my_sum = 0
#     for n in args:
#         my_sum += n
#     return my_sum
#
#
# print(add(1, 2))
#
# print(add(1, 2, 3, 4, 5, 6, 99))


# Kwargs (Keyword Arguments)
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# 2 + 3 * 5 = 25
calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Mitsubishi", model="Lancer")
print(my_car.make)