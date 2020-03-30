value = 10
print(type(value)) # <class 'int'>

conv = str(value)
print(type(conv)) # <class 'str'>

value = "10"
conv = int(value)
print(type(conv))

value = 10
conv = float(value)
print(type(conv))

value = "Hello!"
conv = list(value)
print(type(conv))

value = [1, 2, 3, 10, 20, 30]
conv = tuple(value)
print(type(conv))

value = (10, 20, 40, 10, 25, 30, 45)
conv = frozenset(value)
print(type(conv))

value = 10
conv = bin(value)
print(conv)


value = 10
conv = hex(10)
print(conv)

value = '0b1010' # binary
conv = int(value, 2)
print(conv)

value = '0xa' # hexadecimal
conv = int(value, 16)
print(conv)