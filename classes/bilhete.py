"""

"""""
# Class Product
# Import the generic class
from classes.gclass import Gclass

class Bilhete(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codBilhete','_quantidade','_precoB', '_codFilme', '_nomeC', '_precoFilme', "_precoM"]
    # Class header title
    header = 'Bilhetes'
    # field description for use in, for example, in input form
    des = ['Código do Bilhete','Quantidade','Preço do bilhete', 'Código do Filme', 'Nome do Cliente']
    # Constructor: Called when an object is instantiated
    def __init__(self, codBilhete, quantidade, precoB, codFilme, nomeC, precoFilme, precoM):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:, 
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        self._codBilhete = int(codBilhete)
        self._quantidade = int(quantidade)
        self._precoB = float(precoB)
        self._codFilme=int(codFilme)
        self._nomeC=nomeC
        self._precoFilme=float(precoFilme)
        self._precoM=float(precoM)
        
        #'_codFilme', '_nomeC', '_precoFilme', "_precoM"
        # Add the new object to the Bilhete list
        Bilhete.obj[codBilhete] = self
        Bilhete.lst.append(codBilhete)
    # Object properties
    # codBilhete property getter method
    @property
    def codBilhete(self):
        return self._codBilhete
    # quantidade property getter method
    @property
    def quantidade(self):
        return self._quantidade
    # precoB property getter method
    @property
    def precoB(self):
        return self._precoB
    @precoB.setter
    def precoB(self):
        self._precoB=self._precoM+self._precoFilme
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    # nomeC property getter method
    @property
    def nomeC(self):
        return self._nomeC
    # precoFilme property getter method
    @property
    def precoFilme(self):
        return self._precoFilme
    # precoM property getter method
    @property
    def precoM(self):
        return self._precoM
    