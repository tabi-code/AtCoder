def permutation_mod(n, r, mod):
    if r == 0:
        return 1
    else:
        denominator = 1
        for i in range(n, n - r, -1):
            denominator = (denominator * i) % mod
        return denominator // 1
