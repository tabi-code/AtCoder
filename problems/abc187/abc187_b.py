import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    xy = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            z = (xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0])
            if -1 <= z <= 1:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
