#-*- coding: utf-8 -*-
"""
仅用数字1、2、3、4能组成多少个互不相同且无重复数字的三位数？
请按升序输出上述要求的所有三位数，一行一个。
"""
def solve():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print(i * 100 + j * 10 + k)

if __name__ == "__main__":
    solve()
