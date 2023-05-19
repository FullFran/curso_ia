archiv = 'clase3/prueba.txt'
with open(archiv, 'w') as archivo:
    archivo.write('hola')

with open(archiv, 'a') as archivo:
    archivo.write('\nmundo')
    archivo.writelines('\nnino que hase')

with open(archiv) as archivo:
    string = archivo.read()
    lines = archivo.readlines()
print(string)
print(lines)
for i, line in lines:
    print(f'{i} {line}')
