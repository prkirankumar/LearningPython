import itertools

list1 = [1, 2, 3]
list2 = [4, 5]

result = list(itertools.chain(list1, list2))

print(result)


for i in itertools.count(20, 2):
    if i < 31:
        print(i)
    else:
        break

lam = lambda x: x < 5

result = list(itertools.filterfalse(lam, range(10)))

print(result)