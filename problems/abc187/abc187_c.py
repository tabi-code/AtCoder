import sys
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    d = collections.defaultdict(int)
    for i in range(n):
        s = str(input().rstrip('\n'))
        d[s]
    for k in d.keys():
        if k[0] == "!":
            if k[1:] in d:
                print(k[1:])
                exit()
    print("satisfiable")


if __name__ == '__main__':
    solve()
