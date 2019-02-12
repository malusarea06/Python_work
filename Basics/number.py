list2 = []
bool = True
while bool:
    x = int(input())

    if x >= 0:
        list2.append(x)
    else:
        bool = False


def check_lastdigit(num):
    k = 0
    if num < 100:
        k = num%10

    elif num < 999:
        r = num%100
        k = r%10

    elif num < 9999:
        t = num%1000
        e = t%100
        k = e%10
    return k

for i in list2:
    if i > 10:
        k = check_lastdigit(i)
        if k != 6:
            print(i)
    else:
        print(i)
