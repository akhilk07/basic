num = 123
res = ""
while(num != 0):
    last_digit = num % 10
    res = res + str(last_digit)
    num = num // 10
print(res)


for i in range(1,10):
    if i==3:
        pass
    print(i)