from math import pi

print("%.4f" % pi)

cph = [i for i in range(1, 5)]

print(cph)


cph = [i ** 2 for i in range(1, 15, 5)]

print(cph)

cph = [i ** 2 for i in range(5, 25, 3) if i <= 16]

print(cph)

cph = {x: x * 3 for x in range(9)}

print(cph)

cph = {x / 2.5 for x in range(10, 19)}

print(cph)