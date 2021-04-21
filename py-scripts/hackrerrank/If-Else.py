#!/usr/bin/env python
N = int(input("Favor ingrese numero a evaluar: "))
mod = N % 2
if mod > 0:
    print("Weird")
elif (mod == 0) and (N >= 6) and (N <= 20):
    print("Weird")
elif (mod == 0) and (N <= 5) and (N >= 2):
    print("Not Weird")
else:
    print("Not Weird")
