lam = lambda x, y: x * y

print(lam(2, 5))


lam = lambda list1: [x * y for x in range(1, 5) for y in list1]

print(lam([1, 2]))