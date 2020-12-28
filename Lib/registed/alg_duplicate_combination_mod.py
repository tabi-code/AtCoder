def duplicate_combination_mod(n, r, mod):
    n = n + r - 1
    r = min(n - r, r)
    if r == 0:
        return 1
    else:
        denominator = 1
        for i in range(n, n - r, -1):
            denominator = (denominator * i) % mod
        molecule = 1
        for i in range(1, r + 1):
            molecule = (molecule * i) % mod
        return denominator * pow(molecule, mod - 2, mod) % mod
