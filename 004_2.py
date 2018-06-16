#-*- coding: utf-8 -*-
"""
输入某年某月某日，判断这一天是这一年的第几天？（这题有点难，要花点时间）

输入：共一行，三个整数分别表示年、月、日。保证日期的合法性。
输出：一行一个整数，表示一年的第几天
"""
def is_leap_year(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    year, month, day = input().split(' ')
    year, month, day = int(year), int(month), int(day)
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_count = 0
    for i in range(1, month):
        if i != 2:
            day_count += month_days[i - 1]
        else:
            if is_leap_year(year):
                day_count += 29
            else:
                day_count += 28
    day_count += day
    print(day_count)
