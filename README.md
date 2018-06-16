####  000: 给整数a, b，计算两数的和与积
输入：共一行，两个数字以空格隔开   
输出：第一行输出a+b的和，第二行输出a*b   
    

输入样例1:    
> 1 2

输出样例2:
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