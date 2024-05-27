

from classes.gclass import Gclass
from classes.filme import Filme
import datetime

class Sessão(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1

    # class attributes, identifier attribute must be the first one on the list
    att = ['_codSessao','_codSala', '_dia','_hora','_codFilme','_capacidade']
    #class header title
    header="Sessão"
    #fielde description for use in
    des=["Código Sessão", "Código Sala", "Dia", "Hora", "Código Filme", "Capacidade"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codSessao, codSala,dia,hora, codFilme, capacidade):
        super().__init__()
        # Object attributes
        if codFilme in Filme.lst:
            self._codSessao = str(codSessao)
            self._codSala = str(codSala)
            self._dia = datetime.date.fromisoformat(dia)
            self._hora = hora
            self._codFilme = str(codFilme)
            self._capacidade=capacidade
        else:
            print('O filme', codFilme, 'não existe')
        
        # Add the new object to the Filme list
        Sessão.obj[codFilme] = self
        Sessão.lst.append(codFilme)
    # Object properties
    # codFilme property getter method
    @property
    def codSessao(self):
        return self._codSessao
    @codSessao.setter
    def codSessao(self, precoF):
        self._codSessao = precoF
    # nomeF property getter method
    @property
    def codSala(self):
        return self._codSala
    @codSala.setter
    def codSala(self, precoF):
        self._codSala = precoF
        
    @property
    def dia(self):
        return self._dia
    @dia.setter 
    def dia(self, x):
        self._dia = x
    @property
    def hora(self):
        return self._hora
    @hora.setter 
    def hora(self, x):
        self._hora = x
    # precoF property setter method
    @property
    def codFilme(self):
        return self._codFilme
    @codFilme.setter
    def codFilme(self, precoF):
        self._codFilme = precoF
    @property
    def capacidade(self):
        return self._capacidade
    @capacidade.setter
    def capacidade(self, capacidade):
        self._capacidade = capacidade
    
    
    
    