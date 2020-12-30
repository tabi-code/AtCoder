ql = [[0, ]]
ql = collections.deque(ql)
fq = collections.defaultdict(list)
fq[]
while True:
    if len(ql) != 0:
        cost, yv, xv = ql.popleft()
        for yv, xv in [[yv + 1, xv], [yv - 1, xv], [yv, xv + 1], [yv, xv - 1]]:
            if 0 <= yv < h and 0 <= xv < w:
                if (yv, xv) not in fq:
                    ql.append([cost + 1, yv, xv])
                    fq[yv, xv]
    else:
        break
