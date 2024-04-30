# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:47:41 2024

@author: rodri
"""

from datafile import filename

from classes.cliente import Cliente

Filme.read(filename + 'Filmedata.db')

# obj = Filme.from_string("1;Anyone but You;5")

# print("objeto sem estar gravado ",obj)

# Filme.insert(getattr(obj,Filme.att[0]))

# obj = Filme.from_string("2;Interstellar;3")
# Filme.insert(getattr(obj,Filme.att[0]))


# print("\nLista dos onjetos gravados " ,Filme.lst)


# alterar
obj = Filme.first()
print ("\nPrimeiro objeto gravado ",obj)
obj._nomeF = "Anyone but You"
Filme.update(getattr(obj, Filme.att[0]))

Filme.read(filename + 'Filmedata.db')

print("\nobjectos gravados")    
for code in Filme.lst:
    print(Filme.obj[code])