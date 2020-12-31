import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    a, b = list(map(int, input().rstrip('\n').split()))
    for i in range(1251):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)


if __name__ == '__main__':
    solve()
