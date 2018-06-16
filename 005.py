#-*- coding: utf-8 -*-
"""
输入三个整数x,y,z，请把这三个数由小到大输出。

输入：一行，三个数x,y,z
输出：一行，排序后的三个数，用空格隔开
"""
if __name__ == "__main__":
    x, y, z = input().split(' ')
    x, y, z = int(x), int(y), int(z)
    if x <= y and y <= z:
        print(x, y, z)
    elif x <= z and z <= y:
        print(x, z, y)
    elif y <= x and x <= z:
        print(y, x, z)
    elif y <= z and z <= x:
        print(y, z, x)
    elif z <= x and x <= y:
        print(z, x, y)
    else:
        print(z, y, x)
