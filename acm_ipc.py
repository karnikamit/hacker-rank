N = int(input('N '))
M = int(input('M '))
ppl = []
for i in range(N):
    ppl.append(input('binary len M '))
l = len(ppl)
i = 0
while i< l-2:
    k_topics = []
    for k in ppl[i]:
        for j in ppl[i+1]:
            if k:
                k_topics.append(k)
                if j:
                    k_topics.append(j)
	i += 1
print k_topics
