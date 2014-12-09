#Palindromes Hacker rank problem 5 'The Love letter mystery
'''
palindrome - a word that reads same in backwards.

1. abc --> ab*c* --> ab*a* :: c=>a = 2 steps
2. abcba --> this is a palindrome

'''
cases = int(input('cases:'))
for case in range(cases):
    
    al = list('abcdefghijklmnopqrstuvwxyz')
    let = {}
    for i in range(26): #Forming a dict of alphabets
        let[i] = al[i]
        
    ip = input('string:')   #change this to raw_input for python2.x
    i = len(ip)

    if i%2 == 0:    #spliting the given string into two parts
        a = int(i/2)
    else:
        a = int(i/2)
    b = list(ip[-a:])   #letters req to change
    c = list(ip[:a])    
    steps = []
    
    #counting the steps req to form a palindrome.

    for change in b:
        for letter in c[-1]:
            for key in let:
                if letter == let[key]:
                    break
            for key1 in let:
                if change == let[key1]:
                    break
            
            if key1 > key:
                steps.append(key1-key)
            else:
                steps.append(key-key1)
            c.pop()
    print(sum(steps))
input() #Delete this line before submitting       
    

