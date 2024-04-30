# Class Product
# Import the generic class
from classes.gclass import Gclass
from classes.cliente import Cliente
from classes.filme import Filme

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
        if ncliente in Cliente.lst:
            if codFilme in Filme.lst:
                self._codReview = int(codReview)
                self._nota = int(nota)
                self._ncliente = int(ncliente)
                self._codFilme = int(codFilme)
                Reviews.obj[codReview] = self
                Reviews.lst.append(codReview)

            else:
                print("O código do filme", codFilme, "não encontrado!")
        else:
            print("O número de cliente", ncliente, "não existe!")
        
    # Object properties
    # codReview property getter method
    @property
    def codReview(self):
        return self._codReview
    @codReview.setter
    def codReview(self,x):
        self._codReview=int(x)
    # nota property getter method
    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self,x):
        self._nota=int(x)
    # ncliente property getter method
    @property
    def ncliente(self):
        return self._ncliente
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    
