# hola mundo

# el print es para mostrar algo en pantalla, lo que este entre los parentesis, para texto se coloca entre comillas ""
# podemos usar comas "," para separar textos del mismo print
""" 
este es un comentario tambien 
pero en varias lineas 
"""
# el print es para mostrar datos en pantalla, lo que este dentreo de los parentesis y entre comillas (simples o dobles) se imprimira. 
print("hola mundo")
# #puede haber varios separados por comas ","
print('hola',"mundo")     

''' 
tipos de numero.  
integer: enteros positivo y negativo 
Float: decimales positivos y negativos 
''' 

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)                    
                                                                
# type es para indentificar el tipo o clase
# y estos son los types que existen

print(type(10))                  # Int --------- "Numero Entero"
print(type(3.14))                # Float ------- "Punto Flotante o Numero Decimal"
print(type(1 + 3j))              # Complex ----- "Numero Complejo o Ecuacion"
print(type('Asabeneh'))          # String ------ "Texto (tambien puede abreviarse str)"
print(type([1, 2, 3]))           # List -------- "lista de datos o variables (conservan el type)"
print(type({'name':'Asabeneh'})) # Dictionary -- "diccionario (“Si quiero una variable que agrupe datos y a cada uno darle una etiqueta, uso un diccionario.”)"
print(type({9.8, 3.14, 2.7}))    # Set --------- "conjunto de valores unicos ("no me importa el orden, me importa que no se repitan")"
print(type((9.8, 3.14, 2.7)))    # Tuple ------- "una agrupacion de datos inmutables (que no deben ser alterados o no deben cambiar)"
print(type(3 == 3))              # Bool -------- ""
print(type(3 >= 3))              # Bool

'''

	•	Lista → colección que cambia
	•	Tupla → colección fija
	•	Set → valores únicos
	•	Diccionario → datos etiquetados 
--------------------------------------------
Lista = orden
Tupla = orden fijo
Set = unicidad
Dict = significado

'''


# input(' enter your name: ')   # registra imput (o entrada) de usuario 
# el imput solo registra todo como texto aunque como mas adelante aprendi, puedes registrarlo como otro type(clase) si primero colocas la clase y encierras en parentesis. 
int(input("escribe la fecha:  "))    # asi se muestra el texto al usuario (escribe la fecha:) y python leera la entrada como la clase convertida en este caso un numero entero

''' 
help('keywords') # muestra la lista de keywords
help() #ayuda en base a documentacion acerca de la busqueda, un type, keyword cualquier parte de python

'''
print(type(input))
