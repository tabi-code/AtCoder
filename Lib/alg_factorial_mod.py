def factorial_mod(denominator_no, molecule_list, mod):
    denominator = 1
    for i in range(1, denominator_no + 1):
        denominator = (denominator * i) % mod
    molecule = 1
    for molecule_no in molecule_list:
        for i in range(1, molecule_no + 1):
            molecule = (molecule * i) % mod
    return denominator * pow(molecule, mod - 2, mod) % mod
