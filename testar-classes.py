

from datafile import filename

from classes.reviews import Reviews

from classes.cliente import Cliente

from classes.filme import Filme

from classes.menu import Menu

from classes.userlogin import Userlogin

Userlogin.read(filename + 'Filmedata.db')

# objf=Filme.from_string("3;Fast furious;4")

# Filme.insert(getattr(objf,Filme.att[0]))

# objc=Cliente.from_string("4;Manuel;4")

# Cliente.insert(getattr(objc,Filme.att[0]))

Userlogin.read(filename + 'Filmedata.db')

obj = Userlogin.from_string("User2;cliente;pass11")
#    att = ['_codBilhete','_quantidade','_precoB', '_codFilme', '_ncliente', "_codM"]

print("objeto sem estar gravado ",obj)

Userlogin.insert(getattr(obj,Userlogin.att[0]))

# obj = Reviews.from_string("2;7")
# Reviews.insert(getattr(obj,Reviews.att[0]))


# print("\nLista dos objetos gravados ",Reviews.lst)


# # # alterar
# obj = Reviews.first()
# print ("\nPrimeiro objeto gravado ",obj)
# obj._precoM = "10"
# Reviews.update(getattr(obj, Reviews.att[0]))

# Reviews.read(filename + 'Filmedata.db')

# print("\nobjectos gravados")    
# for code in Reviews.lst:
#     print(Reviews.obj[code])
