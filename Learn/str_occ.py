
str = "amalamagam"
count = 0
l = len(str)
k=0
substring = input()
length = len(substring)
for i in range(0,l):
    strs = str[i:i+length]
    if(substring == strs):
        count = count + 1

print("Occurence of string "+substring+" is : ",count)


