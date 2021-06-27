import sys

def blackjack(n, m):
    card = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if card[i]+card[j]+card[k] > m:
                    continue
                else:
                    sum = max(sum, card[i]+card[j]+card[k])
    return sum



n, m = map(int, sys.stdin.readline().split())
print(blackjack(n, m))
