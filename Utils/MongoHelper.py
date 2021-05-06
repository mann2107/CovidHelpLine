import pymongo
from bson import ObjectId
from Utils import DBConfig
from pprint import pprint


def get_collection(col_name):
    myclient = pymongo.MongoClient(DBConfig.CONNECTION_URL)
    mydb = myclient[DBConfig.DB_NAME]
    mycol = mydb[col_name]
    return mycol


def get(collection_name, criteria, *fields):
    col = get_collection(collection_name)
    response = []
    result = ''
    try:
        if len(fields) > 0:
            result = col.find(criteria, fields)
        else:
            result = col.find(criteria)
    except Exception as e:
        print(e)
        response = None
    for x in result:
        response.append(x)
    return response


def insert(collection_name, **fields):
    col = get_collection(collection_name)
    response = []
    result = ''
    try:
        if bool(fields):
            result = col.insert_one(fields)
        else:
            response = None
    except Exception as e:
        print(e)
        response = None
    return response


def upsert(collection_name, criteria, **fields):
    col = get_collection(collection_name)
    response = []
    result = ''
    try:
        if bool(fields):
            result = col.update(criteria, fields, upsert=True)
        else:
            response = None
    except Exception as e:
        print(e)
        response = None
    return response

