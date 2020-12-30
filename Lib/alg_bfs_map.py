mpl = collections.defaultdict(list)
for i in range():
    mpa, mpb = list(map(int, input().rstrip('\n').split()))
    mpl[mpa-1] += [mpb-1]
    mpl[mpb-1] += [mpa-1]
    
ql = [[0, ]]
ql = collections.deque(ql)
fq = collections.defaultdict(list)
fq[]
while True:
    if len(ql) != 0:
        cost, tmp = ql.popleft()
        for tmv in tmd[tmp]:
            if tmv not in fq:
                ql.append([cost + 1, tmv])
                fq[tmv]
    else:
        break
