import re

from soupsieve import match

zen = """Although never is 
often better than 
*right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation 
is easy to explain, 
it may be a good 
idea.Namespaces 
are one honking 
great idea -- let's 
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."
g = re.findall("t[ow]o", string, re.IGNORECASE)
print(g)

# 数値との一致( grep "[[:digit:]]")を使用する。
"""
$echo 123 hi 34 hello. | grep "[[:digit:]]"
"""

line = "123 hi 34 hello."
f = re.findall("\d", line, re.IGNORECASE)
print(f)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)
