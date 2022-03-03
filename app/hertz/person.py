from faker import Faker



class Person():
    def __init__(self):
        self.fake = Faker()
        self.__uuid = self.uuid()
        self.__first_name = self.first_name()
        self.__last_name = self.last_name()
        self.__phone_number = self.phone_number()
        self.__email_address = self.email_address()


    def first_name(self):
        first_name,*rest  = tuple(word for word in self.fake.name().split())
        return first_name


    def last_name(self):
        first_name,last_name,*rest = tuple(word for word in self.fake.name().split())
        return last_name



    def uuid(self):
        uuid = self.fake.uuid4()
        return uuid



    def phone_number(self):
        phone_number = self.fake.phone_number()
        return phone_number


    def email_address(self):
        email_address = self.fake.email()
        return email_address


    def __iter__(self):
        return iter((self.__first_name,self.__last_name,self.__uuid,self.__phone_number,self.__email_address))



    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r},{!r},{!r})'.format(classname,self.__uuid,self.__first_name,self.__last_name,self.__phone_number,self.__email_address)



