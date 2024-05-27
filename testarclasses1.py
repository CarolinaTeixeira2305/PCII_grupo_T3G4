

from datafile import filename

from classes.cliente import Cliente

Cliente.read(filename + 'Filmedata.db')

from classes.menu import Menu
Cliente.read(filename + 'Filmedata.db')

cname = "Cliente"
cl = eval(cname)

obj = cl.from_string("11;Cliente11;934563445")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("21;Excel1;934563442")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


# alterar
obj = cl.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD11"
Cliente.update(getattr(obj, cl.att[0]))

cl.read(filename + 'Filmedata.db')

print("\nobjectos gravados")    
for code in cl.lst:
    print(cl.obj[code])
