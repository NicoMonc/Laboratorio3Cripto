with open('10_million_password_list_top_100000.txt') as f:
    lines = f.readlines()
print("Largo inicial: "+str(len(lines)))
editado= open("modificado.txt", "a")
for linea in lines:
    if not (linea[0].isdigit()):
        editado.write('{}{}0\n'.format(linea[0].upper(),linea[1:-1]))
with open('modificado.txt') as g:
    lines = g.readlines()
print("Largo final: "+str(len(lines)))
