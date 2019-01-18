#!/usr/bin/env python36
import re

#re.match - determine whether it matches at the beginning of a string (return an object representing the match)
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")

#re.search - find a match of a pattern anywhere in the string
if re.search(pattern, "1spamspamspam"):
   print("Match")
else:
   print("No match")

mmm = re.search(pattern, "eggspamsausage")
if mmm:
    print(mmm.group())
    print(mmm.start())
    print(mmm.end())
    print(mmm.span())

#findall - return a list of all substrings that match a pattern
print(re.findall(pattern, "1spamspamspam"))

#sub - replace all occurrences of the pattern in string with repl, substitute all (unless max provided) occurrences.
line='Hi, My name is Vasya.'
pattern3='Vasya'
newline=re.sub(pattern3,'Petya',line)
print(newline)

