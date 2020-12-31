import sys
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    dq = collections.deque()
    dq.append("b")
    n = int(input().rstrip('\n'))
    s = str(input().rstrip('\n'))
    for i in range(10 ** 20):
        ts = "".join(dq)
        if ts == s:
            print(i)
            exit()
        else:
            if len(ts) > len(s):
                print(-1)
                exit()
            else:
                if i % 3 == 0:
                    dq.appendleft("a")
                    dq.append("c")
                elif i % 3 == 1:
                    dq.append("a")
                    dq.appendleft("c")
                else:
                    dq.append("b")
                    dq.appendleft("b")


if __name__ == '__main__':
    solve()
