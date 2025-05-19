class Coffee:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
         return self._name
  
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Must be a string")
        if len(value) < 3:
            raise ValueError ('NEEDS TO HAVE AT LEAST 3 CHARACTERS')
        self._name=value

   