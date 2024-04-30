"""

"""""
# Class Product
# Import the generic class
from classes.gclass import Gclass

class Reviews(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codReview','_nota','_ncliente', '_codFilme']
    # Class header title
    header = 'Reviews'
    # field description for use in, for example, in input form
    des = ['Código Review','Nota','Número Cliente' , "Código Filme"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codReview, nota, ncliente, codFilme):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        self._codReview = int(codReview)
        self._nota = int(nota)
        self._ncliente = int(ncliente)
        self._codFilme = int(codFilme)
        
        # Add the new object to the Cliente list
        Reviews.obj[codReview] = self
        Reviews.lst.append(codReview)
    # Object properties
    # codReview property getter method
    @property
    def codReview(self):
        return self._codReview
    # nota property getter method
    @property
    def nota(self):
        return self._nota
    # ncliente property getter method
    @property
    def ncliente(self):
        return self._ncliente
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    
