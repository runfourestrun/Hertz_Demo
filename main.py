from hertz import contract,person
from neo4j import GraphDatabase





def get_all_parameters(Object,sample_size:int):
    '''

    :param sample_size: integer, ammount of objects you want to generage
    :param Object: generic, Object whos attributes you want to glean
    :param acceptable_fields: fields that you want to use in the object
    :return: list of dicts representing the objects
    '''
    list_of_dict_object_attributes = []

    for i in range(sample_size):
        object = Object()
        _dict = {key:value for key,value in vars(object).items() if key != 'fake'}
        list_of_dict_object_attributes.append(_dict)
    return list_of_dict_object_attributes




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


def create_contract(tx,batch):
    tx.run(
    '''
    UNWIND $batch as param
    MERGE (c:Contract {id:param._Contract__contract_id,cost:param._Contract__price})
    ''',parameters=batch)


def create_person(tx,batch):
    tx.run(
    '''
    UNWIND $batch as param
    MERGE (c:Customer {id:param._
    ''',parameters=batch)







if __name__ == '__main__':


    uri = 'bolt://localhost:7687'
    driver = GraphDatabase.driver(uri, auth=('neo4j',''))
    sample_size = 5000




    contract_parameters = get_all_parameters(contract.Contract,sample_size=10000)
    person_parameters = get_all_parameters(person.Person,sample_size=200)
    contract_batches = batch_parameters(contract_parameters ,batch_size=1000)
    person_batches = batch_parameters(person_parameters,batch_size=50)



    with driver.session() as session:
        for _batch in contract_batches:
            batch = {}
            batch['batch'] = _batch
            session.write_transaction(create_contract,batch)

        for _batch in person_batches:
            batch = {}
            batch['batch'] = _batch
            session.write_transaction(create_person,batch)




















