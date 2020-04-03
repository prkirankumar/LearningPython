'''
readline()
readlines()
'''

import os

os.getcwd() # gets current working directory

try:
    f = open("c:\\practice\\test.xml", "r")
    print(f.read())
except BaseException as ex:
    print(type(ex))


f = open("c:\\practice\\test.xml", "r")
print(f.readlines()) # returns as list

f = open("c:\\practice\\test.xml", "r")
f.read()
f.seek(10) # ion="1.0" encoding="utf-8" standalone="yes"?> instead of <?xml version="1.0" encoding="utf-8" standalone="yes"?>
print(f.read())

os.system("cls") # screen clear
f = open("c:\\practice\\test.xml", "r")
f.read()
# f.read(10) reathe file from the given position
print(f.read())
print(f.tell())

os.system("cls") # screen clear
f = open("c:\\practice\\test.xml", "r")
f.read(5)
print(f.mode)

f = open("test.txt", "a+")
print(f.mode)


f = open("c:\\practice\\test.txt", "w")
f.write("python")
f.close()
f = open("c:\\practice\\test.txt", "r")
print(f.read())

f = open("c:\\practice\\test.txt", "w")
f.writelines(['scala', ' ', 'and', ' ', 'java'])
f.close()
f = open("c:\\practice\\test.txt", "r")
print(f.read())


with open("c:\\practice\\test.txt", "w") as f:
    f.write("python")

f = open("c:\\practice\\test.txt", "r")
print(f.read())


with open("c:\\practice\\test.txt", "w") as f:
    f.write("python 3.8")

f = open("c:\\practice\\test.txt", "r+")
f.truncate() # deletes all the data in the file
f = open("c:\\practice\\test.txt", "r")
print(f.read())
#######################################
os.system("cls")

os.chdir('C:\\Practice') # changes the current working directory
os.listdir()
os.getcwd()
#######################################
print("using for loop")
for line in open('c:\\practice\\test.xml'):
    print(line,end='')
#####

try:
    f = open("c:\\practice\\test.txt", "r")
    f.detach()
    print(f.read())
except BaseException as ex:
    print(ex)

f = open("c:\\practice\\test.xml", "r")
print(f.fileno())
print(f.isatty())
print(f.readable())

print(f.readline())
print(f.readline(4))
print(f.readline(-1))

###############################
# remove unwanted text from a file name and replace file

def replace(folder_path):
    for path, files in os.walk(folder_path):
        for name in files:
                file_path = os.path.join(path,name)
                file_path_updated=file_path.replace("unwanted text","")
                os.rename(file_path, file_path_updated)
            
replace("C:\\MyFolder")
              

                