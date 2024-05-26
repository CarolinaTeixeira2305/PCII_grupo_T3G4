

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
    att = ["_codM", "_precoM", "_nomeM"]
    # Class header title
    header = 'Menu'
    # field description for use in, for example, in input form
    des = ["Código do Menu", "Preço do Menu", "Nome do Menu"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codM, precoM, nomeM):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:, 
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        self._codM=str(codM)
        self._precoM=float(precoM)
        self._nomeM = str(nomeM)
        # Add the new object to the FilmeFun list
        Menu.obj[codM] = self
        Menu.lst.append(codM)
        
    # Object properties
    # codMenu property getter method
    @property
    def codM(self):
        return self._codM
    # precoM property getter method
    @property
    def precoM(self):
        return self._precoM
    # precoM property setter method
    @precoM.setter
    def precoM(self,x):
        try:
            self._precoM = float(x)
        except ValueError:
            print("O preço do menu deve ser um número.")
            
    @property 
    def nomeM(self):
        return self._nomeM
    @property 
    def Menuobj(self):
        return Menu.obj()