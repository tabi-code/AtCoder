import sys
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, q = list(map(int, input().rstrip('\n').split()))
    mpl = collections.defaultdict(list)
    for i in range(n - 1):
        mpa, mpb = list(map(int, input().rstrip('\n').split()))
        mpl[mpa-1] += [mpb-1]
        mpl[mpb-1] += [mpa-1]
    score = [0] * n
    for i in range(q):
        p, x = list(map(int, input().rstrip('\n').split()))
        score[p-1] += x
    ql = [[0, 0]]
    ql = collections.deque(ql)
    fq = collections.defaultdict(list)
    fq[0]
    while True:
        if len(ql) != 0:
            cost, tmp = ql.popleft()
            for tmn in mpl[tmp]:
                if tmn not in fq:
                    ql.append([cost + 1, tmn])
                    fq[tmn]
                    score[tmn] += score[tmp]
        else:
            break
    print(*score)



if __name__ == '__main__':
    solve()
