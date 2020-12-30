st = "対象文字列"
st_len = len(st)
z_algorithm = [0] * st_len
z_i = 1
z_j = 0
while z_i < st_len:
    while z_i + z_j < st_len and st[z_j] == st[z_i + z_j]:
        z_j += 1
    z_algorithm[z_i] = z_j
    if z_j == 0:
        z_i += 1
        continue
    z_k = 1
    while z_i + z_k < st_len and z_k + z_algorithm[z_k] < z_j:
        z_algorithm[z_i + z_k] = z_algorithm[z_k]
        z_k += 1
    z_i += z_k
    z_j -= z_k
print(z_algorithm)
