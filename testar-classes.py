# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:47:41 2024

@author: rodri
"""

from datafile import filename

from classes.reviews import Reviews

from classes.cliente import Cliente

from classes.filme import Filme

from classes.menu import Menu
Cliente.read(filename + 'Filmedata.db')

# objf=Filme.from_string("3;Fast furious;4")

# Filme.insert(getattr(objf,Filme.att[0]))

# objc=Cliente.from_string("4;Manuel;4")

# Cliente.insert(getattr(objc,Filme.att[0]))

Reviews.read(filename + 'Filmedata.db')

obj = Reviews.from_string("1;5;2;2")
#    att = ['_codBilhete','_quantidade','_precoB', '_codFilme', '_ncliente', "_codM"]

# print("objeto sem estar gravado ",obj)

# Reviews.insert(getattr(obj,Reviews.att[0]))

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
