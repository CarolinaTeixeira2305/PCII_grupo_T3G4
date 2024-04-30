from classes.gclass import Gclass
from classes.filme import Filme
import datetime

class Sessao(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey =1
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
        if codFilme in Filme.lst:
            self._codSessao = int(codSessao)
            self._codSala = int(codSala)
            self._fila = int(fila)
            self._nlugar = int(nlugar)
            self._dia = datetime.date(dia)
            self._hora = hora
            self._codFilme = int(codFilme)
        else:
            print('O filme', codFilme, 'não existe')
        
        # Add the new object to the Filme list
        Sessao.obj[codFilme] = self
        Sessao.lst.append(codFilme)
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
    # precoF property getter method
    @property
    def fila(self):
        return self._fila
    @fila.setter 
    def fila(self, x):
        self._fila = x
    @property
    def nlugar(self):
        return self._nlugar
    @nlugar.setter 
    def nlugar(self, x):
        self._nlugar = x
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
    
