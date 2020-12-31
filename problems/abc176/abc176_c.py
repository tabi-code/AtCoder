import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    mx = 0
    cnt = 0
    for i in range(n):
        if mx > a[i]:
            cnt += mx - a[i]
        mx = max(mx, a[i])
    print(cnt)


if __name__ == '__main__':
    solve()
