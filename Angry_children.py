n = int(input('n '))
k = int(input('k '))
candies = [int(input('candies: ')) for i in range(0,n)]
candies.sort()
candies_k = []
i = 0
for j in range(0, k):
    candies_k.append(candies[i])
    i += 1
min_diff = max(candies_k)-min(candies_k)

print (min_diff)

#input
20
5
4504
1520
5857
4094
4157
3902
822
6643
2422
7288
8245
9948
2822
1784
7802
3142
9739
5629
5413
7232
#op
1335
