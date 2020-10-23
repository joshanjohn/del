def count(file):
    f = open(file,"r")
    low,up,nm = 0,0,0
    line = f.readlines()

    for i in line:
        for j in i:
            if j.islower():
                low += 1
            elif j.isupper():
                up += 1
            elif j.isnumeric():
                nm += 1
    print("Total lower case - {0}\nTotal upper case - {1}\nTotal numbers - {2}".format(low,up,nm))
    print("........FILE.....CLOSED.....")

        
file = input("Enter the file name (example.txt):")
count(file)

