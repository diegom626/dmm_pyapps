#!/usr/bin/env python
intentos = 1
passwd = [4,2,6,4]
while intentos < 11:
    correcto = 0
    incorrect = 0
    print "\n\nNumero de Intento: %s"  %  intentos
    prompt = raw_input("Favor ingrese numero de 4 digitos: ")
    if (len(str(prompt)) == 4) and (prompt.isdigit()):
        lista = [int (i) for i in str(prompt)] 
        print lista
        print "La contrasena ingresada es: %s " % prompt
        intentos = intentos + 1
        for number in range(len(lista)):
            if lista[number] == passwd[number]:
                correcto += 1
            else: incorrect += 1
        print "Digitos correctos: %s" % correcto
        print "Digitos incorrectos: %s\n\n" % incorrect             
        if correcto == 4:
            intentos = 10
            print "Ud. a adivinado la contrasena!: %s" % prompt
    else: 
        print "Ingrese la cantidad de caracteres requeridos y/o validos"
        intentos += 1


