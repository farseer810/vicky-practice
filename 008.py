#-*- coding: utf-8 -*-
"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

输入：一行，正整数n
输出：一行，按上述例子打印分解表达式
"""
if __name__ == "__main__":
    n = int(input())

    i = 2
    expression = ''
    while n != 1:
        if n % i == 0:
            if expression == '':
                expression = str(n) + '=' + str(i)
            else:
                expression += '*' + str(i)
            n = n // i
        else:
            i += 1

    print(expression)
    
