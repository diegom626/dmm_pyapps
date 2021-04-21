#!/usr/bin/env python
import re
f = open('/home/dmunoz/bash-scripts/example.txt', 'r')
lines = f.readlines()
print(lines)
f.close()
f = open('/home/dmunoz/bash-scripts/example.txt', 'w')
# doc = f.read()
inc = 20000
for line in lines:
    search = re.sub(r"(.+):20000", r"\1:"+str(inc), line.strip("\n"))
    if re.search(r"(.+):20000", line.strip("\n")) is None:
        f.write(line.strip("\n"))
        f.write("\n")
    else:
        f.write(search)
        f.write("\n")
        inc += 1
f.close()
# search = re.sub(r"(.+):20000", r"\1:21000", doc)
