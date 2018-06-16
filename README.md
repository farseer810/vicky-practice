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