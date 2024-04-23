# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:38:31 2024

@author: rodri
"""

# Class Product
# Import the generic class
from classes.gclass import Gclass

class Menu(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ["_codMenu", "_precoM", "_codBilhete"]
    # Class header title
    header = 'Menu'
    # field description for use in, for example, in input form
    des = ["Código do Menu", "Preço do Menu", "Código do Bilhete"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codMenu, precoM, codBilhete):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:, 
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        
        self._codMenu=int(codMenu)
        self._precoM=float(precoM)
        self._codBilhete=int(codBilhete)
        
        # Add the new object to the FilmeFun list
        Menu.obj[codMenu] = self
        Menu.lst.append(codMenu)
    # Object properties
    # codMenu property getter method
    @property
    def codMenu(self):
        return self._codMenu
    # precoM property getter method
    @property
    def precoM(self):
        return self._precoM
    # codBilhete property getter method
    @property
    def codBilhete(self):
        return self._codBilhete