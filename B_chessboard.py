import sys

def chess(n, m):
    res = []
    board=[list(map(str, input())) for i in range(n)]
    for i in range(n-7):
        for j in range(m-7):
            Wcount = 0
            Bcount = 0
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a+b) % 2 == 0:
                        if board[a][b] != 'W':
                            Wcount += 1
                        if board[a][b] != 'B':
                            Bcount += 1
                    else:
                        if board[a][b] != 'W':
                            Bcount += 1
                        if board[a][b] != 'B':
                            Wcount += 1
            res.append(Wcount)
            res.append(Bcount)
    return min(res)


n, m = map(int, sys.stdin.readline().split())
print(chess(n, m))