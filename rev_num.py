n = 12345
k = 0

while n:
    k = k*10 + n%10
    n //= 10

print(k)