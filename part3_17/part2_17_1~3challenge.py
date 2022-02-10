import re


line = "The ghost that says boo haunts the loo"
m = re.findall(".oo", line, re.IGNORECASE)
print(m)

"""
$ grep " Dutch" zen.txt
Although that way may not be obvious at first unless you're Dutch.

$ echo "Arizona 479, 501, 870. California 209, 213, 650." | grep "[[:digit:]]"
Arizona 479, 501, 870. California 209, 213, 650.
"""
