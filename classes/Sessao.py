# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:58:32 2024

@author: up202306650
"""
from Classes.gclass import Gclass
import datetime

class Sessao(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codSessao','_codSala','_fila','_nlugar', '_dia','_hora','_codFilme']
    #class header title
    header="Sessao"
    #fielde description for use in
    des=["Código Sessão", "Código Sala", "Fila", "Lugar", "Dia", "Hora", "Código Filme"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codSessao, codSala, fila, nlugar,dia,hora, codFilme):
        super().__init__()
        # Object attributes
        self._codSessao = int(codSessao)
        self._codSala = int(codSala)
        self._fila = int(fila)
        self._nlugar = int(nlugar)
        self._dia = datetime.date(dia)
        self._hora = hora
        self._codFilme = int(codFilme)
        
        # Add the new object to the Filme list
        Sessao.obj[codFilme] = self
        Sessao.lst.append(codFilme)
    # Object properties
    # codFilme property getter method
    @property
    def codSessao(self):
        return self._codSessao
    # nomeF property getter method
    @property
    def codSala(self):
        return self._codSala
    # precoF property getter method
    @property
    def fila(self):
        return self._fila
    # precoF property setter method
    @precoF.setter
    def precoF(self, precoF):
        self._precoF = precoF