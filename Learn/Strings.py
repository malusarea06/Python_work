var = 'My name is aniket'
stock = 'Geeks for Geeks man'
print(stock.rindex('man'))
#print(stock[19-3])




for i in range(10,18):
    string = "%x"%(i)
    print(string,end=" ")
name = "Aniket"


def rotate(input,d):
    LFirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0:len(input)-d]
    Rsecond = input[len(input)-d:]

    print("LEFT ROTATION :",(Lsecond+LFirst))
    print("RIGHT ROTATION : ",(Rsecond+Rfirst))

rotate(name,1)