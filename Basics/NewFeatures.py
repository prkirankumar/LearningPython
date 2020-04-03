# walrus operator :=

# num = [1,2,3,4,5]

# if( (size := len(num1)) < 10 ):
#     print(f”Length of list is small, size={size}”)

# positional only arguments
def func(a, b, c, d):
  print(a,b,c,d)

func(d=2, a=3, b=2, c=6) #Valid - prints 3 2 6 2
func(1,3,4,5) #Valid - prints 1 2 4 5

def func( a,b,/,c,d,*,e,f ):
  print(a,b,c,d,e,f )