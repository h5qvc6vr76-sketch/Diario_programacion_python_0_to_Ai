# Write code below 💖

# preguntamos por cantidades en diferentes monedas
COP=    int(input('Cantidad de "COP" '))   # peso colombia
PEN=    int(input('Cantidad de "PEN" '))   # sol peru
BRL=    int(input('Cantidad de "BRL" '))   # real brazil

# preguntamos por equivalencias en dolares de las monedas anteriores
COP_a_USD= float(input('Tipo de cambio de COP a USD: ')) 
PEN_a_USD= float(input('Tipo de cambio de PEN a USD: '))
BRL_a_USD= float(input('Tipo de cambio de BRL a USD: '))

# definimos formulas
COP_en_USD= COP * COP_a_USD
PEN_en_USD= PEN * PEN_a_USD
BRL_en_USD= BRL * BRL_a_USD

Total= (COP_en_USD + PEN_en_USD + BRL_en_USD) 

# mostramos resultados deseados
print(COP_en_USD)
print(PEN_en_USD)
print(BRL_en_USD)
print('----- Total en USD -----')
print(Total)
