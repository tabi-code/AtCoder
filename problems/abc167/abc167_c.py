import sys
import itertools


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m, x = list(map(int, input().rstrip('\n').split()))
    ls = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
    m_cost = 10 ** 20
    for it_v in itertools.product([True, False], repeat=n):
        cost = 0
        score = [0] * m
        for i in range(n):
            if it_v[i]:
                cost += ls[i][0]
                for j in range(1, m + 1):
                    score[j - 1] += ls[i][j]
        is_ok = True
        for i in range(m):
            if score[i] < x:
                is_ok = False
                break
        if is_ok:
            m_cost = min(m_cost, cost)
    print(m_cost if m_cost != 10 ** 20 else -1)


if __name__ == '__main__':
    solve()
