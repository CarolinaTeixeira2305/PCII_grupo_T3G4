"""

"""""
# Class Product
# Import the generic class
from classes.gclass import Gclass
from classes.filme import Filme
from classes.cliente import Cliente
from classes.menu import Menu

class Bilhete(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codBilhete','_quantidade', '_codFilme']
    # Class header title
    header = 'Bilhetes'
    # field description for use in, for example, in input form
    des = ['Código do Bilhete','Quantidade', 'Código do Filme']
    # Constructor: Called when an object is instantiated
    def __init__(self, codBilhete, quantidade, codFilme):
        super().__init__()
        #Uncomment in case of auto number on
        if codBilhete == 'None':
            codBilhete = Bilhete.getatlist('_codBilhete')
            if codBilhete == []: 
                codBilhete = str(1)
            else:
                 codBilhete = str(max(map(int,Bilhete.getatlist('_code'))) + 1)
        #Check
        if codFilme in Filme.lst:
            #if ncliente in Cliente.lst:
                #if codM in Menu.lst:
                    self._codBilhete = str(codBilhete)
                    self._quantidade = int(quantidade)
                    self._codFilme=str(codFilme)
                    #self._ncliente=str(ncliente)
                    #self._codM=str(codM)
                    # Add the new object to the Bilhete list
                    Bilhete.obj[codBilhete] = self
                    Bilhete.lst.append(codBilhete)
               # else:
                    #print("Código de Menu", codM, "não encontrado!")
           # else:
               # print("Número de cliente", ncliente, "não encontrado!")
        else:
            print("Número de filme", codFilme, "não encontrado!")
                
       
    # Object properties
    # codBilhete property getter method
    @property
    def codBilhete(self):
        return self._codBilhete
    @codBilhete.setter
    def codBilhete(self, codBilhete):
        if codBilhete in Bilhete.lst:
            self._codBilhete=str(codBilhete)
        else:
            print("Codigo Bilhete", codBilhete, "não encontrado")
    # quantidade property getter method
    @property
    def quantidade(self): 
        return self._quantidade
    @quantidade.setter
    def quantidade(self, x):
        self._quantidade=int(x)
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    
    # ncliente property getter method
    @property
    def ncliente(self):
        return self._ncliente
    
    # codM property getter method
    @property
    def codM(self):
        return self._codM
    