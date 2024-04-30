

from Classes.gclass import Gclass
from classes.filme import Filme
import datetime

class Funcionario(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1

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
        if codFilme in Filme.lst:
            self._codF = str(codF)
            self._nomeF = str(nomeF)
            self._codSessao = int(codSessao)
            self._codSala = int(codSala)
            self._dia = datetime.date(dia)
            self._hora = str(hora)
            self._codFilme = str(codFilme)
        else:
            print('O código do filme', codFilme, 'não existe')
        
        # Add the new object to the Filme list
        Funcionario.obj[codF] = self
        Funcionario.lst.append(codF)
    # Object properties
    # codF property getter method
    @property
    def codF(self):
        return self._codF
    @codF.setter 
    def codF(self, x):
        self._codF = x
        
    # nomeF property getter method
    @property
    def nomeF(self):
        return self._nomeF
    @nomeF.setter 
    def nomeF(self, x):
        self._nomeF = x
    # fila property getter method
    @property
    def codSessao(self):
        return self._codSessao
    @codSessao.setter 
    def codSessao(self, x):
        self._codSessao = x
    # lugar property getter method
    @property
    def codSala(self):
        return self._codSala
    @codSala.setter 
    def codSala(self, x):
        self._codSala = x
    # dia property getter method
    @property
    def dia(self):
        return self._dia
    @dia.setter 
    def dia(self, x):
        self._dia = x
    # hora property getter method
    @property
    def hora(self):
        return self._hora
    @hora.setter 
    def hora(self, x):
        self._hora = x
    # codFilme property setter method
    @property
    def codFilme(self):
        return self._codFilme
    @codFilme.setter 
    def codFilme(self, x):
        self._codFilme = x