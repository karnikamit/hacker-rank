__author__ = 'karnikamit'
vowels = ['a', 'e', 'i', 'o', 'u']

ip_string = raw_input('ip ').lower()


def build_words(sentence):
    index = 0
    let = ''
    w = {}
    while index <= len(sentence):
        try:
            let += ip_string[index]
            if let in w:
                w[let] += 1
            else:
                w[let] = 1
            index += 1
        except IndexError:
            break
    final = {word: sentence.count(word) for word in w}
    print final
    return sum(final.values())

built = {}
if ip_string[0] in vowels:
    built[2] = {}
    built[2]['words_score'] = build_words(ip_string)
else:
    built[1] = {}
    built[1]['words_score'] = build_words(ip_string)

print built
