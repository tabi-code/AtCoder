import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    h, w = list(map(int, input().rstrip('\n').split()))
    a = [list(map(int, str(input().rstrip('\n')).split())) for _ in range(h)]
    mn = 10 ** 20
    for i in range(h):
        for j in range(w):
            mn = min(mn, a[i][j])
    cnt = 0
    for i in range(h):
        for j in range(w):
            cnt += a[i][j] - mn
    print(cnt)


if __name__ == '__main__':
    solve()
