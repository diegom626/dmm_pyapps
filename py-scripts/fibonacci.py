#!/usr/bin/env

num = raw_input("Ingrese numero para calcular secuencia: ")
num = int(num)
a_1 = 0
a_2 = 0
count = 1
while count <= num:
    count += 1
    if count <= 2 :
        a_1 = 1
        a_2 = 1
        print a_1
        print a_2
    else:
        a_x = a_2 + a_1
        print a_x
        a_1 = a_2
        a_2 = a_x
        

        
print 
