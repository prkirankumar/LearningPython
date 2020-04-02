import re

s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."

result1 = re.match("Bitcoin", s) 
print(result1.group())

'''
if the string is not found then below error will be thrown
Traceback (most recent call last):
  File "regularexpressions.py", line 6, in <module>
    print(result1.group())
AttributeError: 'NoneType' object has no attribute 'group'
'''

result2 = re.match("Bitcoin", s, re.I)
print(result2.group())  


result3 = re.match(r"B.{6} .{3}", s)
print(result3.group())


result4 = re.match(r"B.{10} .{6}", s) # if . removed  then AttributeError: 'NoneType' object has no attribute 'group'
print(result4.group())

result5 = re.search(r"(\d{4})\s", s)
print(result5.group(1)) # 2009

result6 = re.search(r"(\d{4}),", s)
print(result6.group(1)) # 2017

result7 = re.search(r"(.{3}\s\d\w\w\s\d{4})\s", s)
print(result7.group(1)) # Jan 3rd 2009

result8 = re.search(r"([A-Z]{3})", s)
print(result8.group(1))

result9 = re.search(r"([0-9]\s[A-Z]{3})", s)
print(result9.group(1)) # 1 BTC


result = re.search(r"(\$\d{5}),", s)
print(result.group(1)) # $20000

result = re.search(r"(\$\d{3}[A-Z])\.", s)
print(result.group(1))

result = re.search(r"\s(.{6} .{3} .{2})\s", s)
print(result.group(1))

# result = re.search(r"\$(\d{3},[0-9]{3},\d{3},[0-9]{3}),", s)
# print(result.group(1))

result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s)
print(result.group(1))

result = re.search(r"\s([0-9]{2},[0-9]{3},[0-9]{3}\s.{3}),", s)
print(result.group(1))

result = re.search(r"\s(.{4}\s\d\.\d\d%)", s)
print(result.group(1))

result = re.search(r"\.\d\d, (.{1,}:\s\$\d{2,},\d{2,},\d{2,},\d{2,}), ", s)
print(result.group(1))


result = re.search(r"(\w+ \w+: \d{2}.+? [A-Z]{3}), ", s)
print(result.group(1))

result = re.search(r",([0-9]{3}\.[0-9]{2},\s.)", s)
print(result.group(1))

result = re.findall(r"\s(\d{4})", s)
print(result)

result = re.findall(r"\d{1,}", s)
print(result)

result = re.findall(r"\s(\w{3})\s", s)
print(result)

result = re.findall(r"([A-Z]{1}.+?)\s", s)
print(result)

result = re.findall(r"\s(o.{1})\s", s)
print(result)

result = re.findall(r"\w{8,}", s)
print(result)

result = re.findall(r"\s([ac]\w{2,})\s", s)
print(result)

result = re.sub(r"\s\d{4}", " XXXX", s)
print(result)

result = re.sub(r"\d{1,},*\d*\.\d{1,}", ".", s)
print(result)

result = re.sub(r"[A-Z]{3}", "Bitcoin", s)
print(result)

result = re.sub(r"[0-5]", "8", s)
print(result)

result = re.sub(r"[A-Z]\w{1,}|[6-9]", "W", s)
print(result)