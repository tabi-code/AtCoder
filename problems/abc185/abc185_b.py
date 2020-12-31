import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m, t = list(map(int, input().rstrip('\n').split()))
    tn = n
    pt = 0
    for i in range(m):
        a, b = list(map(int, input().rstrip('\n').split()))
        tn = max(tn - (a - pt), 0)
        pt = b
        if tn == 0:
            print("No")
            exit()
        else:
            tn = min(tn + (b - a), n)
    print("Yes" if tn - (t - pt) > 0 else "No")


if __name__ == '__main__':
    solve()
