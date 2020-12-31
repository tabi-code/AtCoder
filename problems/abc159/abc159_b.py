import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    s = str(input().rstrip('\n'))
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            print("No")
            exit()
    for i in range(len(s) // 2):
        if s[i] != s[-i - 2 - len(s)//2]:
            print("No")
            exit()
        if s[i + 1 + len(s) // 2] != s[-i-1]:
            print("No")
            exit()
    print("Yes")




if __name__ == '__main__':
    solve()
