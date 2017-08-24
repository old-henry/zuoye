
# 1、使用while循环输入 1 2 3 ... 8 9 10
i=1
while i <= 10:
    print(i)
    i+=1

#2、求1-100的所有数的和
s=0
for i in range(101):
    s+=i

print(s)

# 3、输出 1-100 内的所有奇数
for i in range(1,101,2):
    print(i)

# 4、输出 1-100 内的所有偶数
for i in range(2,101,2):
    print(i)

# 5、求1-2+3-4 ... 99的所有数的和
s=0
for i in range(100):
    if i%2 == 0:
        s=s-i
    else:
        s=s+i
print(s)