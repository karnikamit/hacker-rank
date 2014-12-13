cases = int(input())
san = []
for case in range(cases):
    N, K = int(input()), int(input())
    for i in range(N):
        san.append(int(input()))
    a = sum(san)
    if a%K == 0:
        print ('yes')
    else:
        print ('no')        
