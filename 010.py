#-*- coding: utf-8 -*-
"""
输入两个正整数m和n，求其最大公约数和最小公倍数。

输入：一行，m和n
输出：第一行输出最大公约数，第二行输出最小公倍数
"""
def calculate_gcd(m, n): # gcd short for greatest common divisor，最大公约数
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m % n
    return m

if __name__ == '__main__':
    m, n = input().split(' ')
    m, n = int(m), int(n)
    gcd = calculate_gcd(m, n)
    print(gcd)
    print(m * n // gcd)
