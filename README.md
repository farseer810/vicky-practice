####  000: 给整数a, b，计算两数的和与积
输入：共一行，两个数字以空格隔开   
输出：第一行输出a+b的和，第二行输出a*b   
    
输入样例1:    
> 1 2

输出样例1:
> 3    
2 

```python
if __name__ == "__main__":
    """
    line = input() # 读一行字符串
    a, b = line.split(' ') # 以空格分离一行字符串
    a, b = int(a), int(b) # 转换成整数类型
    """
    a, b = input().split(' ') # 读取一行字符串并以空格分开
    a, b = int(a), int(b)
    print(a + b)
    print(a * b)
```

#### 001: 仅用数字1、2、3、4能组成多少个互不相同且无重复数字的三位数？<br/>请按升序输出上述要求的所有三位数，一行一个。
```python
def solve():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print(i * 100 + j * 10 + k)

if __name__ == "__main__":
    solve()
```

#### 002: 企业发放的奖金根据利润提成。利润(n)低于或等于10万元时，奖金可提10%；<br/>利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；<br/>20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；<br/>60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成。<br/>从键盘输入当月利润n，求应发放奖金总数？
输入：共一行，数字n   
输出：共一行，奖金总数(若不为整数，则四舍五入取整)
   
输入样例1:    
> 1150000

输出样例1:
> 41000

```python
def calculate_bonus(n):
    if n <= 100000:
        bonus = n * 0.1
    elif n <= 200000:
        bonus = 0.1 * 100000 + (n - 100000) * 0.075
    elif n <= 400000:
        bonus = 0.1 * 100000 + 0.075 * 100000 + (n - 200000) * 0.05
    elif n <= 600000:
        bonus = 0.1 * 100000 + 0.075 * 100000 + 0.05 * 200000 + (n - 400000) * 0.03
    elif n <= 1000000:
        bonus = 0.1 * 100000 + 0.075 * 100000 + 0.05 * 200000 + 0.03 * 200000 + (n - 600000) * 0.015
    else:
        bonus = 0.1 * 100000 + 0.075 * 100000 + 0.05 * 200000 + 0.03 * 200000 + 0.015 * 400000 + (n - 1000000) * 0.01
    return round(bonus)

if __name__ == "__main__":
    n = float(input())
    print(calculate_bonus(n))
```

#### 003: 输入整数n，判断是否为完全平方数？
输入：共一行，整数n   
输出：如果是完全平方数，输出yes；否则输出no   

输入样例1:    
> 9

输出样例1:
> yes

输入样例2:    
> -1

输出样例2:
> no

```python
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
```

#### 004_1: 输入某年，判断这一年是否为闰年（2月有29天）？
输入：一行，年份n   
输出：闰年输出yes，否则输出no   

输入样例1:    
> 1600

输出样例1:
> yes

```python
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
```

#### 004_2: 输入某年某月某日，判断这一天是这一年的第几天？（这题有点难，要花点时间）
输入：共一行，三个整数分别表示年、月、日。保证日期的合法性。   
输出：一行一个整数，表示一年的第几天   

输入样例1:    
> 1995 3 1

输出样例1:
> 60

输入样例2:    
> 2000 3 1

输出样例2:
> 61

```python
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
```

#### 005: 输入三个整数x,y,z，请把这三个数由小到大输出。
输入：一行，三个数x,y,z   
输出：一行，排序后的三个数，用空格隔开   

输入样例1:    
> 2 1 3

输出样例1:
> 1 2 3

```python
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
```

#### 006: 判断101-200之间有多少个素数，并输出所有素数。
输出：第一行，素数个数；第二行开始按升序输出素数，一行一个数   

```python
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
```

#### 007: 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。<br/>例如：153是一个“水仙花数”，因为153=1^3＋5^3＋3^3
输出：第一行，水仙花数个数；第二行开始每行表示一个水仙花数，升序输出   

```python
if __name__ == "__main__":
    narcissistic_number_list = []
    for i in range(100, 1000):
        digit1, digit2, digit3 = i // 100, i % 100 // 10, i % 10
        if digit1 ** 3 + digit2 ** 3 + digit3 ** 3 == i:
            narcissistic_number_list.append(i)
    
    print(len(narcissistic_number_list))
    for i in narcissistic_number_list:
        print(i)
```

#### 008: 将一个正整数分解质因数。例如：输入90,打印出90=2\*3\*3\*5。
输入：一行，正整数n   
输出：一行，按上述例子打印分解表达式   

```python
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
```

#### 009: 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
输入：一行，分数n(0 <= n <= 100)   
输出：一行，分数级别   

```python
if __name__ == "__main__":
    n = float(input())
    if n >= 90:
        print('A')
    elif n >= 60:
        print('B')
    else:
        print('C')
```

#### 010: 输入两个正整数m和n，求其最大公约数和最小公倍数。
输入：一行，m和n   
输出：第一行输出最大公约数，第二行输出最小公倍数   

```python
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
```
