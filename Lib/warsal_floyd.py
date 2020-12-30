wn = list(map(int, input().rstrip('\n').split()))
inf = 10 ** 13
wl = [[inf] * wn for _ in range(wn)]
for i in range(wn):
    wl[i][i] = 0

for i in range(wn):
    wa, wb, wc = list(map(int, input().rstrip('\n').split()))
    wl[wa - 1][wb - 1] = wc
    wl[wb - 1][wa - 1] = wc

for i in range(wn):
    for j in range(wn):
        for k in range(wn):
            wl[j][k] = min(wl[j][k], wl[j][i] + wl[i][k])
