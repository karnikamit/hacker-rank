N = int(input())
rocks = []
a = ('abcdefghijklmnopqrstuvwxyz')
a_dic = {}
for i in range(26):
    a_dic[i] = a[i]
for rock in range(N):
    r1 = raw_input('rock string')
    rocks.append(r1)
i = 0
element = {}
while i < len(rocks):
    for k in rocks[i]:
        for key in a_dic:
            if k == a_dic[key]:
                element[key] += 1
                break
    i += 1
print element
    
