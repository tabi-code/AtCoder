cor_v = -1
inc_v = 10 ** 20
while cor_v - inc_v > 1:
    bin_v = (cor_v + inc_v) // 2
    cost = 0
    #条件を満たすcostを全検索

    #costが制約を満たすか
    if cost <= bin_v:
        cor_v = bin_v
    else:
        inc_v = bin_v
print(cor_v)
