class Customer:
    def __init__(self,name):
        self.name =name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("DATA MUST BE A STRING")
        if not (1 <= len(value) <=15):
            raise ValueError("IT SHOULD BE BETWEEN 1 TO 15 CHARACTERS")
        
        self._name=value