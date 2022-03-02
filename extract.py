#!/usr/bin/env python
import requests
import pandas as pd
import os
from constructors import Constructor
from engine import session
from sqlalchemy import text
from datetime import datetime


def query_api(endpoint:str, params:None):
    """ Get Data From a JSON API """
    url = "https://ergast.com/api/{}.json?limit={}".format(endpoint,params)
    response = requests.get(url)
    return response.json()['MRData']

def f1():
    """ Get Formula 1 Data """
    return query_api('f1', 1)['RaceTable']['Races']

def constructors():
    return query_api('f1/constructors',2)['ConstructorTable']['Constructors']

def driver():
    return query_api('f1/drivers',1)['DriverTable']['Drivers']

def truncate_table(table_name):
    """
    Ensure that "table_name" table is always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text(f"DELETE FROM {table_name};")
    )
    session.commit()

def bulk_insert_constructor(data):
    """ Bulk Insert Data into Constructor Table """
    constructor_objects = []
    for row in data:
        constructor_objects.append(
            Constructor(
                constructorId = row['constructorId'],
                url = row['url'],
                name = row['name'],
                nationality = row['nationality']
            )
        )
    session.bulk_save_objects(constructor_objects)
    session.commit()

for x in driver():
    print(x)

for x in f1():
    print(x)

for x in constructors():
    print(x.keys())

truncate_table('constructor')
bulk_insert_constructor(constructors())

cmd = f"git add . && git commit -m '{datetime.now()}'"
os.system(cmd)
