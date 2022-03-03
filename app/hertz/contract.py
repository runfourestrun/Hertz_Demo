import faker
from faker import Faker
from random import choices


class Contract():

    def __init__(self):
        self.fake = Faker()
        self.__contract_id = self.contract_id()
        self.__price = self.price()
        self.__contract_expiration_date = self.contract_expiration_date()
        self.__pickup_city,self.__pickup_state = self.pickup_city()
        self.__dropoff_city,self.__dropoff_state = self.__pickup_city,self.__pickup_state
        self.__car_category = self.car_category()


    def contract_id(self):
        contract_id = self.fake.uuid4()
        return contract_id

    def car_category(self):
        car_categories = ["Convertible", "Sedan", " Pickup", "Van/Minivan", "SUV", " Wagon", "Coupe", "Hatchback"]
        weighted_probabilities = [.05, .35, .1, .01, .35, .05, .04, .05]
        choice = choices(car_categories, weighted_probabilities, k=1)
        selection = choice[0]
        return selection



    def price(self):
        transaction_cost = self.fake.random_int(200, 500)
        casted_transaction_cost = '${:,.2f}'.format(transaction_cost)
        return casted_transaction_cost


    def contract_expiration_date(self):
        for date in self.fake.time_series(start_date='now', end_date='+30d'):
            datetime, precision = date
            date = datetime.date()
            return date


    def pickup_city(self):
       *address, city, state, zip = self.fake.address().split()
       return (city,state)





    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r},{!r},{!r},{!r},{!r})'.format(classname,self.__contract_id,self.__price,self.__contract_expiration_date,self.__pickup_city,self.__pickup_state,self.__dropoff_city,self.__dropoff_state,self.__car_category)


    def __iter__(self):
        return iter((self.__contract_id,self.__price,self.__contract_expiration_date,self.__pickup_city,self.__pickup_state,self.__dropoff_city,self.__dropoff_state))









