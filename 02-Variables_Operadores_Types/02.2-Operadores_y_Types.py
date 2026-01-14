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

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'> # Int ------------- "Numero Entero"

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'> # Float ----------- "Punto Flotante o Numero Decimal"

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'> # String ----------- "Texto (tambien puede abreviarse str)"

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'> # Bool ----------- "booleano ("tipo de dato con solo dos valores "True o False" representa condiciones logicas y toma de deciciones(ejemplo: comparaciones)")"

my_set_var = {7, 5, 8}
print(type(my_set_var))  # <class 'set'> # Set ----------------- "conjunto de valores unicos ("no me importa el orden, me importa que no se repitan")"

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'> # Dictionary -- "diccionario (“Si quiero una variable que agrupe datos y a cada uno darle una etiqueta, uso un diccionario.”)"

my_tuple_var = (7, 5, 8)
print(type(my_tuple_var))  # <class 'tuple'> # Tuple ----------- "una agrupacion de datos inmutables (que no deben ser alterados o no deben cambiar)"

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'> # Range ----------- "range en Python es una clase que se usa para generar una secuencia de números hasta el numero indicado desde el cero o se especifica inicio y final"

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'> # List ------------------- "lista de datos o variables (conservan el type)"

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>  # None --------- "None se usa para indicar que una variable o función no tiene valor."
'''
--------------------------------------------
Lista = orden → colección que cambia
Tupla = orden fijo → colección fija
Set = unicidad → valores únicos
Diccionario = significado → datos etiquetados 
'''