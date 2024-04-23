from Classes.gclass import Gclass

class Filme(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codFilme','_nomeF','_precoF']
    #class header title
    header="Films"
    #fielde description for use in
    des=["Code", "Name", "Preco"]
    # Constructor: Called when an object is instantiated
    def __init__(self, codFilme, nomeF, precoF):
        super().__init__()
        # Object attributes
        if codFilme not in Filme.lst:
            self._codFilme = int(codFilme)
            self._nomeF = nomeF
            self._precoF = float(precoF)
            # Add the new object to the Filme list
            Filme.obj[codFilme] = self
            Filme.lst.append(codFilme)
        else:
            print("Código Filme", codFilme, "já existe!")
    # Object properties
    # codFilme property getter method
    @property
    def codFilme(self):
        return self._codFilme
    
    # nomeF property getter method
    @property
    def nomeF(self):
        return self._nomeF
    # precoF property getter method
    @property
    def precoF(self):
        return self._precoF
    # precoF property setter method
    @precoF.setter
    def precoF(self, precoF):
        self._precoF = float(precoF)