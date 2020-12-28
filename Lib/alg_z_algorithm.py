zs = $TS$
zln = len(zs)
zl = [0] * zln
zi = 1
zj = 0
while zi < zln:
    while zi + zj < zln and zs[zj] == zs[zi+zj]:
        zj += 1
    zl[zi] = zj
    if zj == 0:
        zi += 1
        continue
    zk = 1
    while zi + zk < zln and zk + zl[zk] < zj:
        zl[zi+zk] = zl[zk]
        zk += 1
    zi += zk
    zj -= zk
