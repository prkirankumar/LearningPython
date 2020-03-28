#                                                     ****** Indexing *****


'''
You can access a single item of a Python sequence (such as string, tuple, or list) with the corresponding integer indices. 
Indices in Python are zero-based. This means the index 0 corresponds to the first (leftmost) item of a sequence, 1 to the second item, and so on.
Indices are provided inside the brackets, that is with the syntax sequence[index]

Python provides the possibility to use negative integer indices as well. This appears to be very useful in practice, 
especially when you want to access the last (rightmost) item of a sequence.

The index -1 corresponds to the last item, -2 to the second last, and so on
'''


my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[-2]) # s

my_tuple = (1, 2, 4, 8, 16, 32, 64, 128)
print(my_tuple[5]) # 32

my_list=[1, 2, 4, 8, 16, 32, 64, 128]
print(my_list[4]) # 16

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[7]) # ,
print(my_string[-10]) # w
print(my_string.index("B")) # 26
print(my_string.count("o")) # 5
print(my_string.upper()) # IN 2010, SOMEONE PAID 10K BITCOIN FOR TWO PIZZAS.
print(my_string.find("Bitcoin")) # 26
print(my_string.startswith("X")) # False
print(my_string.startswith("I")) # True
print(my_string.swapcase()) # iN 2010, SOMEONE PAID 10K bITCOIN FOR TWO PIZZAS.
print(my_string.replace(" ", "$")) # In$2010,$someone$paid$10k$Bitcoin$for$two$pizzas.
print(my_string.replace("i", "btc"))
print(my_string.split(",")) # ['In 2010', ' someone paid 10k Bitcoin for two pizzas.']
print("&".join(my_string)) # I&n& &2&0&1&0&,& &s&o&m&e&o&n&e& &p&a&i&d& &1&0&k& &B&i&t&c&o&i&n& &f&o&r& &t&w&o& &p&i&z&z&a&s&.

my_other_string = "Poor guy!"

print(my_string + my_other_string) # In 2010, someone paid 10k Bitcoin for two pizzas.Poor guy!
print(my_string.title()) # In 2010, Someone Paid 10K Bitcoin For Two Pizzas.


my_string = "In %s, someone paid %s %s for two pizzas."
print(my_string % ("2010", "10k", "Bitcoin")) # In 2010, someone paid 10k Bitcoin for two pizzas.

my_string = "In {}, someone paid {} {} for two pizzas."
print(my_string.format("2010", "10k", "Bitcoin")) # In 2010, someone paid 10k Bitcoin for two pizzas.
