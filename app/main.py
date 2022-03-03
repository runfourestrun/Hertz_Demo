from app.hertz.person import Person
from app.hertz.contract import Contract
from neo4j import GraphDatabase
from util.timing import timing








@timing
def get_all_parameters(Object,sample_size:int):
    '''

    :param sample_size: integer, amount of objects you want to generage
    :param Object: generic, Object whos attributes you want to glean
    :param acceptable_fields: fields that you want to use in the object
    :return: list of dicts representing the objects
    '''
    list_of_dict_object_attributes = []

    for i in range(sample_size):
        object = Object()
        _dict = {key:value for key,value in vars(object).items() if key != 'fake' }
        list_of_dict_object_attributes.append(_dict)
    return list_of_dict_object_attributes





@timing
def batch_parameters(parameters:list,batch_size:int):
    '''
    Chunks a list into smaller sublists. The idea here is to take create batches or chunks of parameters.
    :param parameters: input parameters
    :param chunk_size: size of sublists
    :return: list of lists. sublists contain a fixed number of elements (the last sublist will just contain the remainder)
    '''
    chunks = (parameters[x:x+batch_size] for x in range(0, len(parameters),batch_size))
    return chunks





'''
Cypher Transaction Functions
'''

@timing
def create_contract(tx,batch):
    tx.run(
    '''
    UNWIND $batch as param
    MERGE (c:Contract {id:param._Contract__contract_id,cost:param._Contract__price})
    WITH param,c
    MATCH (cat:Category {id:param._Contract__car_category})
    MERGE (c) - [:INCLUDES] -> (cat)
    ''',parameters=batch)


@timing
def create_person(tx,batch):
    tx.run(
    '''
    UNWIND $batch as param
    MERGE (c:Customer {id:param._Person__uuid,first_name:param._Person__first_name,last_name:param._Person__last_name,phone_number:param._Person__phone_number,email_address:param._Person__email_address})
    ''',parameters=batch)


@timing
def create_cars_and_category(tx):
    tx.run(
        '''
         CALL apoc.periodic.iterate (
        
            'CALL apoc.load.csv("Car_Model_List.csv", {header:true}) yield map as row',
            '
            MERGE (a:Automobile {id: row["objectId"], make: row["Make"], year:row["Year"], model:row["Model"]})
            WITH a, split(row["Category"],",") as categories
            UNWIND categories as category
            MERGE (c:Category {id:category}) 
            MERGE (a) - [:IS_IN] -> (c)
            '
    , {batchSize:10,parallel:true})
    '''
    )








if __name__ == '__main__':


    uri = 'bolt://localhost:7687'
    driver = GraphDatabase.driver(uri, auth=('neo4j','Reddit123!'))




    contract_parameters = get_all_parameters(Contract,sample_size=1000)
    person_parameters = get_all_parameters(Person,sample_size=2000)
    contract_batches = batch_parameters(contract_parameters ,batch_size=1000)
    person_batches = batch_parameters(person_parameters,batch_size=2000)



    with driver.session() as session:

        session.write_transaction(create_cars_and_category)

        for _batch in contract_batches:
            batch = {}
            batch['batch'] = _batch
            session.write_transaction(create_contract,batch)

        for _batch in person_batches:
            batch = {}
            batch['batch'] = _batch
            session.write_transaction(create_person,batch)



















