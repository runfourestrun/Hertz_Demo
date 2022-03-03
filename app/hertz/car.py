
class Car:
    def __init__(self,make,model,category,year):
        self.make = make
        self.model = model
        self.category = category
        self.year = year



    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r},{!r},)'.format(classname,self.make,self.model,self.category,self.year)

    def __iter__(self):
        return iter((self.__contract_id,self.make,self.model,self.category,self.year))



    @classmethod
    def from_csv(cls,file):
        with open(file, 'rb') as f:
            line = f.readline()





