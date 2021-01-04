import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    a, b = list(map(str, str(input().rstrip('\n')).split()))
    a = sum([int(v) for v in a])
    b = sum([int(v) for v in b])
    print(max(a, b))


if __name__ == '__main__':
    solve()
