def main () :
    n, m = tuple(int(n) for n in input().split())
    edges = tuple(tuple(int(n) for n in input().split()) for i in range(m))
    matrix = [[False for i in range(n+1)]
         for j in range(n+1)]
    for edge in edges :
        matrix[edge[0]][edge[1]] = True
        matrix[edge[1]][edge[0]] = True

    for i in range(n+1) :
        matrix[i][i] = True

    team1 = set()
    team2 = set()

    for i in range(1, n+1) :
        if i not in team1 :
            if i not in team2 :
                team1.add(i)
                in1 = True
            else :
                in1 = False
        else :
            if i in team2 :
                print(-1)
                return
            else :
                in1 = True

        if in1 :
            for j in range(1, n+1) :
                if not matrix[i][j] :
                    team2.add(j)

        else :
            for j in range(1, n+1) :
                if not matrix[i][j] :
                    team1.add(j)

    if len(team2) == 0 :
        a = team1.pop()
        team2.add(a)
    print(len(team1))
    print(' '.join((str(n) for n in team1)))
    print(' '.join((str(n) for n in team2)))

main()
