
n,m = map(int, input().split())

def solve(s):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1, n+1):            
        solve(s + [i])

solve([])