import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    ab = []
    takahashi = 0
    aoki = 0
    for i in range(n):
        a, b = list(map(int, input().rstrip('\n').split()))
        aoki += a
        ab.append([2 * a + b, a, b])
    ab.sort(reverse=True)
    cnt = 0
    for dif, a, b in ab:
        cnt += 1
        takahashi += a + b
        aoki -= a
        if takahashi > aoki:
            print(cnt)
            exit()


if __name__ == '__main__':
    solve()
