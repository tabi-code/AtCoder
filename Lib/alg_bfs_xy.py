ql = [[0, $FQ$]]
ql = collections.deque(ql)
fq = collections.defaultdict(list)
fq[$FQ$]
while True:
    if len(ql) != 0:
        cost, xv, yv = ql.popleft()
        for xv, yv in [[xv + 1, yv], [xv - 1, yv], [xv, yv + 1], [xv, yv - 1]]:
            if 0 <= xv < $H$ and 0 <= yv < $W$:
                if (xv, yv) not in fq:
                    ql.append([cost + 1, xv, yv])
                    fq[xv, yv]
    else:
        break