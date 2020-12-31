import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    k, s = list(map(int, input().rstrip('\n').split()))
    cnt = 0
    for i in range(k + 1):
        for j in range(k + 1):
            if 0 <= s - i - j <= k:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
