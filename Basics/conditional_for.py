x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in x:
    print(i)

for i in x:
    print(i%3)

for i in sorted(x,reverse=True):
    print(i)

for i in x:
    print(i / 2)
else:
    print("Great job!")

for i in x:
    print(x.index(i))

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

for i in x:
    if i > 20:
        print(i * 10)

x = [2, 4, 6]
y = [5, 10]

for i in x:
    for j in y:
        print(i * j)
print("-----")
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for j in y:
        if j < 12:
            print(i * j)
print("-----")
for i in x:
    for j in y:
        if i> 5 and j < 12:
            print(i * j)

print("-----")
for i in x:
    for j in y:
        if j <= 10:
            print(i * j)
        else:
            print(i * j ** 2)

print("-----")
x = "cryptocurrency"
y = "blockchain"

for i in x:
    if i in y:
        print(i * 2)

print("-----")
my_range = range(9)

for i in my_range:
    if 3 <= i <= 7:
        print(i * my_range[1]) # i * 1 , 1 is index

print("-----")
for x in range(1,11,2):
    print(x)

for i in range(1,11,2):
    if 3 <= i <= 8:
        print(i * range(1,11,2)[-1])
    else:
        print("Outside!")

print("-----")
for i in range(5,25,5): # 5 10 15 20
    if 10 <= i <= 21:
        print(i * range(5,25,5)[-2])
    else:
        print("Outside!")
else:
    print("The end!")

print("-----")

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)

print("-----")
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
        print(i)
        break
    print(j)

print("-----")
for i in x:
    for j in y:
        if i % 2 == 0:
            break
            print(i * j)
        print(i)
    print(j)

print("-----")
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            continue
        print(i)
    print(j)

print("-----")
for i in x:
    for j in y:
        if i % 2 == 0:
            continue
            print(i * j)
        print(i)
    print(j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

for i in x:
    for j in y:
        if i % 2 == 0:
            print(x[1] * y[1])