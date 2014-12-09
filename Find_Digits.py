cases = int(input())
for i in range(cases):
    b = 0
    n = int(input())
    a = list(map(int, str(n)))
    if len(a) >1:
        for i in a:
            if i == 0:
                pass
            elif n%i == 0:
                b +=1
        print (b)
            

