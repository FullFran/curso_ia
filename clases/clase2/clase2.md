# Control de flujo en python

## Bloque de codigo: 
(se ejecuta de arriba abajo.)
Algo está dentro de algo con la indentación.

## Condicionales:
Las condiciones son booleanos.

## Bucles:
Bucles while y bucles for.
break rompe el bucle y continue se salta el código de debajo y empieza de nuevo 
el bucle. (ojo con el orden de las cosas.)
range(inicio, fin, salto) '''de fin acaba en uno antes del que pones'''

creamos diccionario:
dct= {'PATATA':'tuberculo',
       'PERA':'fruta', 
    }
puedo iterar en un diccionario:
for key, item in dct.items():
    print(key,item)
for i, elem in enumerate(dct):
    print(i,elem)
    
lis_1=[]