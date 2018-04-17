n = int(input())
lst = [tuple(int(a) for a in input().split()) for i in range(n)]
s = sum(t[0]*t[1] for t in lst)
for t in lst :
    print(round(t[0]*t[1]/s, 12))
