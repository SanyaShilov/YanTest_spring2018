# Time Limit Exceed on about 44th test

import bisect

def f (lw, word, remembered_word) :
    s = 0
    for i in range(min(lw, len(remembered_word))) :
        if word[i] == remembered_word[i] :
            s += 1
        else :
            break
    if s < lw :
        return s + 1
    return s

n = int(input())
words = input().split()
remembered_words = []
l = 0
count = 0
for word in words :
    lw = len(word)
    i = bisect.bisect_left(remembered_words, word)
    if i < l :
        if remembered_words[i] == word :

            if i == 0 :
                if l == 1 :
                    count += 1
                else :
                    count += f(lw, word, remembered_words[i+1])

            elif i == l-1 :
                count += f(lw, word, remembered_words[i-1])

            else :
                count += max(f(lw, word, remembered_words[i-1]),
                             f(lw, word, remembered_words[i+1]))
            continue
        
    count += lw
    remembered_words.insert(i, word)
    l += 1

print(count)
