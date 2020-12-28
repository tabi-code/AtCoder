tmd = collections.defaultdict(list)
for i in range($N$):
    tma, tmb = list(map(int, input().rstrip('\n').split()))
    tmd[tma-1] += [tmb-1]
    tmd[tmb-1] += [tma-1]
    
ql = [[0, $FQ$]]
ql = collections.deque(ql)
fq = collections.defaultdict(list)
fq[$FQ$]
while True:
    if len(ql) != 0:
        cost, tmp = ql.popleft()
        for tmv in tmd[tmp]:
            if tmv not in fq:
                ql.append([cost + 1, tmv])
                fq[tmv]
    else:
        break