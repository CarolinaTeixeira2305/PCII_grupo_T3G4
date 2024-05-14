

# Class Product
# Import the generic class
from classes.gclass import Gclass
from classes.filme import Filme
from classes.funcionario import Funcionario

class FilmeFun(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 2
    # class attributes, identifier attribute must be the first one on the list
    att = ["_codFilme", "_codF"]
    # Class header title
    header = 'FilmeFun'
    # field description for use in, for example, in input form
    des = ['Código do Filme', 'Código do Funcionário']
    # Constructor: Called when an object is instantiated
    def __init__(self, codFilme, codF):
        super().__init__()
        # Uncomment in case of auto number on
        # if code == 'None':
        #     codes = Product.getatlist('_code')
        #     if codes == []:, 
        #         code = str(1)
        #     else:
        #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
        # Object attributes
        if codFilme in Filme:
            if codF in Funcionario:
                
                self._codFilme=str(codFilme)
                self._codF=str(codF)
                
                # Add the new object to the FilmeFun list
                FilmeFun.obj[codFilme] = self
                FilmeFun.lst.append(codFilme)
            else:
                print ("O código do funcionário", codF, "náo existe!")
        else:
            print("O Código do filme", codFilme, "não existe!")
    # Object properties
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    
    # codF property getter method
    @property
    def codF(self):
        return self._codF
    