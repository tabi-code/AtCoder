import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    h = list(map(int, input().rstrip('\n').split()))
    ls = [True] * n
    for i in range(m):
        a, b = list(map(int, input().rstrip('\n').split()))
        if h[a - 1] == h[b - 1]:
            ls[b - 1] = ls[a - 1] = False
        else:
            if h[a - 1] < h[b - 1]:
                a, b = b, a
            ls[b - 1] = False
    print(ls.count(True))


if __name__ == '__main__':
    solve()
