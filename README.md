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