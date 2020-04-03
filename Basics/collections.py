'''
Counter, NamedTuple, DefaultDict, OrderedDict

The ‘collections’ module in Python that implements special container datatypes.
These provide alternatives to Python’s general-purpose built-in containers.


defaultdict - This function returns a default value for it.
OrderedDict - order in which the key-value pairs were added


FAQ : namedtuple vs tuple
'''
#import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple

print(issubclass(Counter,dict) and issubclass(defaultdict,dict) and issubclass(OrderedDict,dict))
print(type(namedtuple)) # function

c=Counter({'a':3,'b':2,'c':1})
print(c) # Counter({'a': 3, 'b': 2, 'c': 1})

c=Counter()
c.update("kirankumar")
print(c)
print(c["k"])

for i in c.elements():
    print(f"{i}: {c[i]}")

print(c.most_common(2))
c["k"]=5
print(c.most_common(2))


c1=Counter('hello')
c2=Counter('help')
print(c1+c2)

d=defaultdict(lambda :35)
print(d) # defaultdict(<function <lambda> at 0x000001D5B0B85430>, {})

d['Ayushi']=95
d['Bree']=89
d['Leo']=90.5
d['Adam']
print(d)


d=defaultdict(list)
for i,j in [('a',(1,2)),('b',(3,4)),('c',(5,6))]:
    d[i].append(j)
print(d)


o=OrderedDict()
o['a']=3
o['c']=1
o['b']=4
print(o)

o.move_to_end('c',last=False)
print(o)
o.popitem()



colors=namedtuple('colors','r g b')
red=colors(r=255,g=0,b=0)
print(red.r)
print(red.g)
print(red.b)
red._replace(g=200)
print(red.g)
print(red)

# converting into dictionary
red._asdict()
