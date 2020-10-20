# print number of upper , lower case and number in text file

f = open("sample.txt")
data = f.readlines ()

for i in data:
    print(i)
    a='X'
    if a in i:
        print("yes")
    else:
        print("No")
