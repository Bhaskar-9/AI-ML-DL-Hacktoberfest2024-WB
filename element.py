# Python3 code to demonstrate working of
# Strings list intersection
# Using reduce() + lambda + Counter()
from functools import reduce
from collections import Counter

# initializing list
test_list = ["geek", "gfgk", "king"]

# printing original list
print("The original list is : " + str(test_list))

# using & operator to perform intersection
res = reduce(lambda a, b: a & b, (Counter(ele) for ele in test_list[1:]),
			Counter(test_list[0]))

# printing result
print("String intersection and frequency : " + str(dict(res)))
