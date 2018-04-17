def solve (a, b, c) :
        res = (-b + (b*b - 4*a*c)**0.5)/2/a
        if not isinstance(res, float) : # may be complex
            return 0
        return res

def solve_w (d, k, b) :
	return solve(49/2, 7*d - 5*k + 7/2, d*d/2 + d/2 - b)

def f (d) :
    return d * (d+1) // 2

def main () :
    k, m, d = tuple(int(n) for n in input().split())
    d -= 1
    reading_today = 1
    books = m
    day = 0
    while d != 0 :
        if d < 5 :
            books += k
        books -= reading_today
        if books < 0 :
            print(day)
            return 0
        reading_today += 1
        d = (d + 1) % 7
        day += 1

    w = int(round(solve_w(day, k, books), 8))
    readed = f(7*w + day) - f(day)
    books = books + 5*w*k - readed
    day += 7*w
    reading_today = day + 1
    while True :
        if d < 5 :
            books += k
        books -= reading_today
        if books < 0 :
            print(day)
            return 0
        reading_today += 1
        d = (d + 1) % 7
        day += 1

main()
