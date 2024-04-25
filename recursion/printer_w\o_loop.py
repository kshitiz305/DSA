'''Print a number from 0 to 10 without using loop'''


def printer(n,i):
    if i > n:
        return 
    print(i)
    printer(n,i+1)

printer(10,0)
