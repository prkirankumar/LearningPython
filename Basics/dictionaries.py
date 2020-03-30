'''             { } or dict()

Separate keys from values with a colon(:), and a pair from another by a comma(,). Finally, put it all in curly braces.
It isn’t necessary to use the same kind of keys (or values) for a dictionary in Python.

dictionary cannot contain the same key twice.
'''
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
print(type(crypto))
value = crypto[4]

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
value = crypto.get(4)
print(value)

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
crypto[4] = "Cardano"
print(crypto[4])

crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
crypto[6] = "Monero" 
print(crypto[6])
print(len(crypto))
#print(crypto[7]) # KeyError
#print(len(crypto)) # wont execute as the previous line throwed exception


del crypto[3]
print(crypto)
crypto.pop(4) # if not found KeyError
print(crypto)

check = 7 not in crypto
print(check)

result = crypto.items()
print(list(result))
# 

add = sum(crypto)
print(add)

val = crypto.values()
print(list(val))

print(list())
print(list(crypto.keys())) # [1, 2, 5, 6]
print(crypto.keys()) # dict_keys([1, 2, 5, 6])
print(min(crypto)) # 1

crypto.clear()
print(crypto) # {}

mydict={x*x:x for x in range(8)}
print(mydict)


print(dict(([1,2],[2,4],[3,6])))


dict2={1:2,1:3,1:4,2:4} # same key holding multiple values
print(dict2)  # {1:4,2:4} 

# an empty dictionary and adding elements later
animals={}
type(animals)
animals[1]='dog'
animals[2]='cat'
animals[3]='ferret'
print(animals)


print(animals[2]) # accessing through key   
print(animals.get(2)) # get(key)



crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
print(len(crypto))
crypto.popitem()
print(len(crypto))
print(crypto)