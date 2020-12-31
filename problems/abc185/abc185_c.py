import sys


def combination(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    else:
        denominator = 1
        for i in range(n, n - r, -1):
            denominator = (denominator * i)
        molecule = 1
        for i in range(1, r + 1):
            molecule = (molecule * i)
        return denominator // molecule


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    l = int(input().rstrip('\n'))
    print(combination(l - 1, 11))


if __name__ == '__main__':
    solve()
