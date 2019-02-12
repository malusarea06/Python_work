def adder(x):
    def add(y):
        return x+y
    return add

plus = adder(9)
print(plus(3))

list = [['A','N','I'],['K','E','T']]
print(list[1][2])