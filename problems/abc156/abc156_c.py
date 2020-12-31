import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    x = list(map(int, input().rstrip('\n').split()))
    mn = 10 ** 20
    for i in range(101):
        cost = 0
        for v in x:
            cost += (v - i) ** 2
        mn = min(mn, cost)
    print(mn)


if __name__ == '__main__':
    solve()
