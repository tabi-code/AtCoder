import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    k, n = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    mn = k - (k - a[-1] + a[0])
    for i in range(1, n):
        mn = min(mn, k - a[i] + a[i - 1])
    print(mn)


if __name__ == '__main__':
    solve()
