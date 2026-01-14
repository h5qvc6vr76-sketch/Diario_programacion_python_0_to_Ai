''' 
tipos de numero.  
integer: enteros positivo y negativo 
Float: decimales positivos y negativos 
''' 
# Operaciones u operadores

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
print(type(3 == 3))              # Bool -------- "booleano ("tipo de dato con solo dos valores "True o False" representa condiciones logicas y toma de deciciones(ejemplo: comparaciones)")"
print(type(3 >= 3))              # Bool -------- "booleano (" == ")"

'''

	•	Lista → colección que cambia
	•	Tupla → colección fija
	•	Set → valores únicos
	•	Diccionario → datos etiquetados 
--------------------------------------------
Lista = orden
Tupla = orden fijo
Set = unicidad
Diccionario = significado

'''