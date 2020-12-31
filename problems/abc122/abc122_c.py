import sys
import itertools


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, q = list(map(int, input().rstrip('\n').split()))
    s = str(input().rstrip('\n'))
    ls = [0] * n
    for i in range(1, n):
        if s[i] == "C" and s[i-1] == "A":
            ls[i] += 1
    ls = list(itertools.accumulate(ls))
    for i in range(q):
        l, r = list(map(int, input().rstrip('\n').split()))
        print(ls[r - 1] - ls[l - 1])


if __name__ == '__main__':
    solve()
