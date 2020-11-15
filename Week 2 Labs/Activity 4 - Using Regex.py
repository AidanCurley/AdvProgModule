"""create regular expressions to do the following:

Find the word ‘shrieked’
Find the word ‘bleak’
Count the number of words that contain ‘pp’
Change all the exclamations marks (!) to hash symbols (#)
Identify all the words that start with a ‘t” but do not end with an ‘e’, case should be ignored here."""

import re

path = "C:/Users/redye/MASTERS YORK/Advanced Programming/Week 2 Labs/"
filename = "The_Raven.txt"
file = open(path + filename, encoding="UTF8")
the_raven = ""

for line in file:
    the_raven += line

print("\nResults")
print(f"Looking for shrieked. Found: {re.search('s[a-z]{6}d', the_raven).group(0)}")
print(f"Is 'bleak' in The Raven? Answer: {'bleak' in the_raven}")
print(f"Number of words containing 'pp': {len(re.findall('[a-zA-Z]*pp[a-z]*', the_raven))}")
print("All words that start with t and do not end in e: ", end="")
print(re.findall("\\b[T|t][\w]*(?<!e)\\b", the_raven))

print("Change ! to #: ")
print(re.sub("!", "#", the_raven))



