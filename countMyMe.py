def countMyMe(file):
    f = open(file,"r")
    count = 0
    line = f.readlines()
    for i in line:
        if 'my' in i:
            count+=1
        elif 'me' in i:
            count+=1
    print("Count of Me/My in file : {}".format(count))
    

        
file = input("Enter the file name (example.txt):")
countMyMe(file)

