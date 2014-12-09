import time
start = time.time()
cases = int(input())
for i in range(cases):
    str_in = raw_input()
    string = list(str_in)
    a,b = 0, 0
    while a< len(string)-1:
        if string[a] == string[a+1]:
            b += 1
        a += 1
    print b
print time.time()-start,'sec'
