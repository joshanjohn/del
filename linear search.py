def main(lst,n):
    def check():
        for i  in range(len(lst)):
            if lst[i] == n:
                print(f'{n} found at position - ',lst.index(lst[i])+1)
                return True
    if not check():
        print('not found')
l = [20,10,50,60,30,74,85,65]
n = int(input('Enter the number to search : '))
main(l,n)
