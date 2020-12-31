import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    a = list(map(int, input().rstrip('\n').split()))
    print(min(a))


if __name__ == '__main__':
    solve()
