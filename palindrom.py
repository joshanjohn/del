def palin(st):
    return st == st[::-1]
st = input("Enter string : ")
result = palin(st)

if result:
    print("string {} is palindrom".format(st))
else:
    print("string {} is not palindrom".format(st))
