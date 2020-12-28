import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    cnt = 0
    dl = [pow(8, i) for i in range(5, -1, -1)]
    for i in range(1, n + 1):
        if str(i).count("7") == 0:
            mod_v = i
            is_ok = True
            for dv in dl:
                div_v, mod_v = divmod(mod_v, dv)
                if div_v == 7:
                    is_ok = False
                    break
            if is_ok and mod_v != 7:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
