"""

"""""
# Class Product
# Import the generic class
from classes.gclass import Gclass

class Cliente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_ncliente','_nomeC','_telemovel']
    # Class header title
    header = 'Cliente'
    # field description for use in, for example, in input form
    des = ['Número','Nome','Telemóvel']
    # Constructor: Called when an object is instantiated
    def __init__(self, ncliente, nomeC, telemovel):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        if ncliente in Cliente.lst:
            print("Número de cliente", ncliente, "já existe!")
        else:
            self._ncliente = str(ncliente)
            self._nomeC = nomeC
            self._telemovel = str(telemovel)
            # Add the new object to the Cliente list
            Cliente.obj[ncliente] = self
            Cliente.lst.append(ncliente)
    # Object properties
    # ncliente property getter method
    @property
    def ncliente(self):
        return self._ncliente
    # ncliente property setter method
    @ncliente.setter
    def ncliente(self, x):
        self._ncliente=x
    # nomeC property getter method
    @property
    def nomeC(self):
        return self._nomeC
    # nomeC property setter method
    @nomeC.setter
    def nomeC(self, x):
        self._nomeC=x
    # telemovel property getter method
    @property
    def telemovel(self):
        return self._telemovel
    # telemovel property setter method
    @telemovel.setter
    def telemovel(self, x):
        self._telemovel=str(x)
    
    