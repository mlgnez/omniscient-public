import azure.cosmos as cosmos
import azure.cosmos.cosmos_client as cosmos_client
import datetime
import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', ''),
    'master_key': os.environ.get('ACCOUNT_KEY', '=='),
    'database_id': os.environ.get('COSMOS_DATABASE', ''),
    'container_id': os.environ.get('COSMOS_CONTAINER', ''),
}


HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
CONTAINER_ID = settings['container_id']


def upload_server(write, ip):
    print("Uploading", ip)

    try:
        client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart",
                                            user_agent_overwrite=True)

        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)

        container.create_item(body=write)

    except Exception:
        print("Error uploading server, returning NulL")
        return None


def read_server(ip):
    print("Reading Server", ip)

    try:
        client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart",
                                            user_agent_overwrite=True)

        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)

        response = container.read_item(item=ip, partition_key=ip)

        return response
    except Exception:
        print("Error Reading Server. Returning NULL")
        return None


def get_all_servers():
    print("Getting All Servers")

    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)

    db = client.get_database_client(DATABASE_ID)
    container = db.get_container_client(CONTAINER_ID)

    response = container.read_all_items()

    print(response)

    return response


def read_items(maxcount):
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)

    db = client.get_database_client(DATABASE_ID)
    container = db.get_container_client(CONTAINER_ID)

    return list(container.read_all_items(max_item_count=100))



def replace_item(container, doc_id, account_number):
    print('\nReplace an Item\n')

    read_item = container.read_item(item=doc_id, partition_key=account_number)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.replace_item(item=read_item, body=read_item)

    print('Replaced Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def upsert_item(container, doc_id, account_number):
    print('\nUpserting an item\n')

    read_item = container.read_item(item=doc_id, partition_key=account_number)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.upsert_item(body=read_item)

    print('Upserted Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def delete_server(ip):
    print("Deleting Server", ip)

    try:
        client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart",
                                            user_agent_overwrite=True)

        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)

        response = container.delete_item(item=ip, partition_key=ip)
    except Exception:
        print("Error deleting server, returning NonULLl")
        return None