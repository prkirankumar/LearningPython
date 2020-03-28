my_var = 10 #type integer 
print(type(my_var)) # <class 'int'>
my_var = "Hello" #type string 
print(type(my_var)) # <class 'str'>
my_var = True #type boolean 
print(type(my_var)) # <class 'bool'>

num1 = 13.67
num2 = int(num1)
print(type(num2))

num1 = 25
num2 = 8
num3 = num1 % num2

print(num3 == 1) # True

num1 = 10
num2 = 3
num3 = num1 ** num2  # 10 * 10 * 10 

print(num3 == 250 * 4) # True

num1 = 5
num2 = 2
num3 = num1 // num2 #integer division, number of times divisible

print(num3 == 5 % 3) # True

num1 = -11
num2 = abs(num1)

print(num2 == 11) # True


num1 = 10
num2 = 5
num3 = pow(num1, num2)

print(num3 == 100000) # True


result = ((25 % 7 + 10 / 2) % 3 == 0) and ((abs(-19) / 2 - 2) > 9)
print(25 % 7 + 10/2) # 9
print(abs(-19) / 2 - 2) # 7.5
print(result) # False

result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1) or (66 % 20 + 2 > 2 ** 3) # True or False
print(pow(2, abs(3)), 9) # 8 9
print(66 % 20 + 2 > 2 ** 3) # False
print(result) # True

result = bool(150 % (10 ** 2 / 2))
print(150 % (10 ** 2 / 2)) # 0.0
print(result) # False

