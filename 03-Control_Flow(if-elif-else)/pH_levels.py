"""
aqui usamos operadores de comparacion, son los siguientes:
"==" -- igual a
"!=" -- no igual a
">"  -- mayor que
"<"  -- menor que 
">=" -- mayor o igual a
"<=" -- menor o igual a

"""

# en python hay que respetar sangrias, estas marcan bloques de codigo (escalones) que marcan el orden de ejecucion


pH= int(input('Ingresa el valor de pH:  '))

if pH < 1 or pH > 14:
    print('pH invalido')
else:
    if pH > 7:
     print('Basico')
    elif pH < 7:
     print("Acido")
    else: 
     print('Neutro') 




