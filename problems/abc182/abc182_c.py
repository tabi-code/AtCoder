import sys
import itertools


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = str(input().rstrip('\n'))
    mn = 10 ** 20
    for it_v in itertools.product([True, False], repeat=len(n)):
        t = 0
        for i in range(len(n)):
            if it_v[i]:
                t += int(n[i])
        if t % 3 == 0:
            c = it_v.count(False)
            if c < len(n):
                mn = min(mn, it_v.count(False))
    print(mn if mn != 10 ** 20 else -1)


if __name__ == '__main__':
    solve()
