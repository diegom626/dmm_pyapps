#!/usr/bin/env python
import re

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]

list = []
for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host
list = [tuple[0] for tuple in tuples]

print list[0]