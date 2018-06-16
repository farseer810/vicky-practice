#-*- coding: utf-8 -*-
"""
输入整数n，判断是否为完全平方数？

输入：共一行，整数n
输出：如果是完全平方数，输出yes；否则输出no
"""
def is_perfect_square(n):
    if n >= 0 and int(n ** 0.5) ** 2 == n:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    if is_perfect_square(n):
        print('yes')
    else:
        print('no')
