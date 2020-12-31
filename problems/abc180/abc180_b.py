import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    x = list(map(int, input().rstrip('\n').split()))
    m, u, c = 0, 0, 0
    for v in x:
        m += abs(v)
        u += pow(v, 2)
        c = max(c, abs(v))
    print(*[m, u ** 0.5, c], sep="\n")


if __name__ == '__main__':
    solve()
