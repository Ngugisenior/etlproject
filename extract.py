#!/usr/bin/env python
import requests
import pandas as pd
import os
from commit import cmd
from constructors import Constructor
from drivers import Driver
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

def bulk_insert_driver(data):
    """ Bulk Insert Data into Constructor Table """
    driver_objects = []
    for row in data:
        driver_objects.append(
            Driver(
                driverId = row['driverId'],
                url = row['url'],
                givenName = row['givenName'],
                familyName = row['familyName'],
                dateOfBirth = row['dateOfBirth'],
                nationality = row['nationality']
            )
        )
    session.bulk_save_objects(driver_objects)
    session.commit()

for x in driver():
    print(x.values())

for x in f1():
    print(x)

truncate_table('constructor')
truncate_table('driver')

bulk_insert_constructor(constructors())
bulk_insert_driver(driver())



os.system(cmd)