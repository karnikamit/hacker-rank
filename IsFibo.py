cases =int(input('cases: '))
for i in range(cases):
    n = int(input('integer to test: '))
    first = 0
    second = 1
    fib_series = []
    fib_no = 0
    while fib_no in range(n+1):
        fib_no = first + second
        fib_series.append(fib_no)
        first = second
        second = fib_no
        
    if n < 10**10:
        if n in fib_series:
            Is = True
        else:
            Is = False
    
        if Is:
            print 'IsFibo'
        else:
            print 'IsNotFibo'

'''
import math
for i in range(int(input())):
    n=int(input())
    r1 = math.sqrt(5*n**2+4)
    r2 = math.sqrt(5*n**2-4)
    isSquare = r1%1 == 0 or r2%1==0
    if(isSquare):
        print "IsFibo"
    else:
        print "IsNotFibo"
'''

