def ten(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input("Enter number : "))
values = []
for i in ten(n):
    values.append(str(i))
print(",".join(values))
