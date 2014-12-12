s = input('sentence: ')
a = ('abcdefghijklmnopqrstuvwxyz')
al = list(a)
AL = list(a.upper())
a_dic = {}
A_dic = {}
chk = {}
for i in range(26):
    a_dic[i] = al[i]
    A_dic[i] = AL[i]
for i in s:
    for key in a_dic:
        if i == a_dic[key] or i == A_dic[key]:
            chk[key] = 1
            break
if len(chk)== 26:
    print 'pangram'
else:
    print 'not pangram'
