#-*- coding: utf-8 -*-
"""
判断101-200之间有多少个素数，并输出所有素数。

输出：第一行，素数个数；第二行开始按升序输出素数，一行一个数
"""
def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    prime_number_list = []
    for i in range(100, 201):
        if is_prime_number(i):
            prime_number_list.append(i)
    print(len(prime_number_list))
    for i in prime_number_list:
        print(i)
    