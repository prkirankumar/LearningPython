a=(lambda :print("Hello"))()
print(a)

o=lambda x=1,y=2,z=3:x+y+z
print(o(2,3))


a,b=1,2
y=lambda a,b:a+b
print(y())

y=lambda :2+3
print(y())

# y=lambda a,b: # gets exception, if we are not passing expression