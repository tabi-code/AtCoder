import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    a.sort(reverse=True)
    sa = sum(a)
    for i in range(m):
        if a[i] < (1 / (m * 4)) * sa:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    solve()
