#  examples 

x = "The days of Python 2 are almost over. Python 3 is the king now."

if len(x) >= 50:
    print("True!")

if type(x) is str and x.startswith("T"):
    print("True!")

if "z" in x or x.count("y") >= 2:
    print("True!")

if x.index("f") < 10:
    print("True!")
else:
    print("False!")

if x[-3:].isdigit():
    print("True!")
else:
    print("False!")

x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if len(x) >= 8 and type(x[6]) is float:
    print("True!")
else:
    print("False!")

if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print("True!")
else:
    print("False!")

if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print("True!")
else:
    print("False!")

# if max(x[:3]) <= min(x[3:6]):     # TypeError: '<' not supported between instances of 'int' and 'list'
#     print("True!!!")
# else:
#     print("False!!!")


x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
if max(x[:3]) <= min(x[3:6]):      
    print("True!!!")
else:
    print("False!!!")

if x.count(115) >= 1 or x.index(115) == 0:
    print("True!")
else:
    print("False!")


x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[5] == "Perl" or  len(x) % 5 < 2:  # Perl or 2<2  True or False
    print("True!")
else:
    print("False!")

if 3 in x and sorted(x.values())[0] == "C#": # True and True
#    print(sorted(x.values())[-1][-1])
    print("True!")
else:
     print("False!")

if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")

if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print(sorted(x.keys())) # [1, 2, 3, 4, 5, 6, 7]
    print("True!!")
else:
    print("False!!")

if sum(x) < len(x[1] + x[2] + x[3] + x[4] + x[5]): # 28 <28
    print("True!")
else:
    print("False!")

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
print(x) # [[0, 1, 2, 3, 4], [5, 6, 7, 8], [1, 4, 7]]

if x[0][2] < 2:
    print("True!")
elif x[0][4] == 5:
    print("False!")
else:
    print("None!")

if x[2][2] < 6:
    print("True!")
elif x[1][0] == 5:
    print("False!")
else:
    print("None!")

if x[0][-1] > 3:
    print("True!")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None!")

if len(x[0]) >= 5:
    print("True!")
elif len(x[1]) == 4:
    print("False!")
else:
    print("None!")


if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")

if max(x[0]) - x[2][1] == x[0][0]:
    print("True!!")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("False!")
elif sum(x[2]) % 2 == 0:
    print("Maybe!")
else:
    print("None!")


if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("True!")
elif len(x[0]) * 2 < sum(x[2]):
    print("False!")

# print(x[0][-3:])# 2 3 4
# print(x[2][-3:])# 1 4 7
# print(x[1][-3:])# 6 7 8 

if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("True!")
elif len(x[0]) * 2 < sum(x[2]):
    print("False!")

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[1][1] in x[4]: # y in Ruby
    print("True!")
else:
    print("False!")


if x[3][-2] == x[5][0]:
    print("True!")
else:
    print("False!")

print(min(x.values()))  #   C#
print(len(min(x.values())))  #   2

if len(min(x.values())) == x[3].count("a"): # 2==2
    print("True!")
else:
    print("False!")