
data = open("/Users/aniketmalusare/Documents/input.txt","r")

lines = data.readlines()

data.close()

nline = list(lines)

def trailing_whitespace(line1):
    c = 0
    for i in line1:
        str = len(i)-1
        if (str == 28) and i[str].isspace():
            print(i[:str])

trailing_whitespace(nline)
