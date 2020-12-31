import sys
import itertools


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    ls = [0] * (n + 1)
    for i in range(m):
        l, r = list(map(int, input().rstrip('\n').split()))
        ls[l-1] += 1
        ls[r] -= 1
    ls = list(itertools.accumulate(ls))
    print(ls.count(m))


if __name__ == '__main__':
    solve()
