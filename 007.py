#-*- coding: utf-8 -*-
"""
打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个“水仙花数”，因为153=1^3＋5^3＋3^3

输出：第一行，水仙花数个数；第二行开始每行表示一个水仙花数，升序输出
"""
if __name__ == "__main__":
    narcissistic_number_list = []
    for i in range(100, 1000):
        digit1, digit2, digit3 = i // 100, i % 100 // 10, i % 10
        if digit1 ** 3 + digit2 ** 3 + digit3 ** 3 == i:
            narcissistic_number_list.append(i)
    
    print(len(narcissistic_number_list))
    for i in narcissistic_number_list:
        print(i)
