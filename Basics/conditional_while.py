x = 0

while x <= 5:
    print(x ** 2)
    x = x + 1

x=1
while x <= 5:
    print(x * 10)
    x = x + 1
else:
    print("Done!")

x = 10
while x <= 15 and x % 5 == 0:
    print(x + 10)
    x = x + 1

x = -7

while x < 0:
    print(abs(x))
    x = x + 1

x = 5
y = 2

while x >= 5 and x < 10:
    print(x * y)
    x = x + 1
else:
    print(x / y)

print("-----")
x = 5

while x <= 11:
    if x == 10:
        print("x is 10!")
        x = x + 1
    else:
        print(x * 11)
        x = x + 1   