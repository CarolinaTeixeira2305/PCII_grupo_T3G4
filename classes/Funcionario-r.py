# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:58:32 2024

@author: up202306650
"""
from Classes.gclass import Gclass
import datetime

class Funcionario(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codF','_nomeF','_codSessao','_codSala', '_dia','_hora','_codFilme']
    #class header title
    header="Sessao"
    #fielde description for use in
    des=["Código Funcionário", "Nome Funcionário", "Código Sessão", "Código Sala", "Dia", "Hora", "Código Filme"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codF, nomeF, codSessao, codSala,dia,hora, codFilme):
        super().__init__()
        # Object attributes
        self._codF = int(codF)
        self._nomeF = str(nomeF)
        self._codSessao = int(codSessao)
        self._codSala = int(codSala)
        self._dia = datetime.date(dia)
        self._hora = str(hora)
        self._codFilme = int(codFilme)
        
        # Add the new object to the Filme list
        Funcionario.obj[codF] = self
        Funcionario.lst.append(codF)
    # Object properties
    # codF property getter method
    @property
    def codF(self):
        return self._codF
    # nomeF property getter method
    @property
    def nomeF(self):
        return self._nomeF
    # fila property getter method
    @property
    def codSessao(self):
        return self._codSessao
    # lugar property getter method
    @property
    def codSala(self):
        return self._codSala
    # dia property getter method
    @property
    def dia(self):
        return self._dia
    # hora property getter method
    @property
    def hora(self):
        return self._hora
    # codFilme property setter method
    @property
    def codFilme(self):
        return self._codFilme
