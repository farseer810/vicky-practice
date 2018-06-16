#-*- coding: utf-8 -*-
"""
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

输入：一行，分数n(0 <= n <= 100)
输出：一行，分数级别
"""
if __name__ == "__main__":
    n = float(input())
    if n >= 90:
        print('A')
    elif n >= 60:
        print('B')
    else:
        print('C')
