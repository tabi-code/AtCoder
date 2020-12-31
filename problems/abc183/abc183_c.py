import sys
import itertools


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, input().rstrip('\n').split()))
    t = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    cnt = 0
    for it_v in itertools.permutations(range(1, n)):
        cost = 0
        lp = 0
        for v in it_v:
            cost += t[lp][v]
            lp = v
        if k == cost + t[lp][0]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
