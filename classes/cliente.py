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
        self._ncliente = int(ncliente)
        self._nomeC = nomeC
        self._telemovel = int(telemovel)
        # Add the new object to the Cliente list
        Cliente.obj[ncliente] = self
        Cliente.lst.append(ncliente)
    # Object properties
    # ncliente property getter method
    @property
    def ncliente(self):
        return self._ncliente
    # nomeC property getter method
    @property
    def nomeC(self):
        return self._nomeC
    # telemovel property getter method
    @property
    def telemovel(self):
        return self._telemovel
    