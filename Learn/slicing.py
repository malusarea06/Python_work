def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
print("list1 = ",list1)
list2 = extendList(123,[])
print("list2 = ",list2)
list3 = extendList('a')
print("list3 = ",list3)



def yell(text):
    return text.upper() + "!"

bark = yell

list = [bark,str.lower,str.capitalize]

klerk = list[2]
print(list)
print(list[0]("ani"))


for i in list:
    print(i("and"))

def ger(func):
    greeting = func('Hello this is function passing')
    print(greeting)

ger(yell)

def whisper(text):
    return text.lower() + '!'

ger(whisper)




