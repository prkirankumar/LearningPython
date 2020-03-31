'''

'''



try:
    print(25 % 0)
except ZeroDivisionError:
    print("Zero!") # Zero

try:
    for i in range(3):
        print(3/i)
except:
    print("You divided by 0")
    print("This prints because the exception was handled")

try:
    print(25 % 5 ** 5 + 5) # 30
except:
    print("Bug!")
else:
    print("Clean!") # Clean


x = [1, 9, 17, 32]

try:
    print(x[3] % 3 ** 5 + x[4]) # dont' have index 4 
except ZeroDivisionError:
    print("Zero Error!")
except IndexError:
    print("Index Error!") # Index Error


try:
    print(25 % 5 ** 5 + 5) # 30
except ZeroDivisionError:
    print("Zero!")
else:
    print("Clean!") # Clean
finally:
    print("Finish!") # Finish

# handling multiple exceptions
a,b=1,0
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")

# handling multiple excepions in one except
try:
    print('10'+10)
    print(1/0)
except (TypeError,ZeroDivisionError):
    print("Invalid input")

# generic except after all exceptions
try:
    print('1'+1)
    print(sum)
    print(1/0)
except NameError:
    print("sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something went wrong")

#####
a,b=int(input("enter a value : ")),int(input("enter b value : "))
try:
    if b==0:
        raise ZeroDivisionError
except:
   print("You divided by 0")
print("Will this print?")

#

try:
    print('outer try block')
    try:
        print('inner try block')
        print(10/0)
    # except ZeroDivisionError:
    #     print('inner except block')
    except ValueError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')



try:
    print('try')
    print(10/0)
except:
    print('except')
else:
    print('else')
finally:
    print('finally')


f=None
try:
    f=open('abc.txt','r')
except:
    print('some problem while location file')
else:
    print('file opened successfuly')
    print('the data presented in the file is ')
    print('#'*30)
    print(f.read())
finally:
    print('finally')
    if f is not None:
        f.close()

## custom exception

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input('Enter Age : '))

if age>60:
    raise TooOldException('Please wait some more time, definitely you will get best match')
elif age<18:
    raise TooOldException('Your age already crossed marriage age, no chance of getting married')
else:
    print('you will get match details soon')

### using identifier

try:
    x=int(input('Enter first number: '))
    y=int(input('Enter second number: '))
    print('The Result : ',x/y)
except BaseException as e:
    print("Exception Type : ",type(e))
    print("Exception Type : ",e.__class__)
    print("Exception Class Name : ",e.__class__.__name__)
    print("Exception Description : ",e)






