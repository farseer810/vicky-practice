#-*- coding: utf-8 -*-
"""
输入某年，判断这一年是否为闰年（2月有29天）？

输入：一行，年份n
输出：闰年输出yes，否则输出no
"""
def is_leap_year(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    if is_leap_year(n):
        print('yes')
    else:
        print('no')
