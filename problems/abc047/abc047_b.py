import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    w, h, n = list(map(int, input().rstrip('\n').split()))
    xs, xe, ys, ye = 0, w, 0, h
    for i in range(n):
        x, y, a = list(map(int, input().rstrip('\n').split()))
        if a == 1:
            xs = max(xs, x)
        elif a == 2:
            xe = min(xe, x)
        elif a == 3:
            ys = max(ys, y)
        else:
            ye = min(ye, y)
    print(max(0, xe - xs) * max(0, ye - ys))


if __name__ == '__main__':
    solve()
