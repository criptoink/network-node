import datetime
import json

from peewee import *
from playhouse.shortcuts import dict_to_model, model_to_dict
from playhouse.sqlcipher_ext import *
from playhouse.sqlite_ext import *

db = SqlCipherDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class NodeInConnections (BaseModel):
    host = CharField()
    owner = CharField()
    join_at = DateTimeField(null=True)
    last_interaction = DateTimeField(null=True)

class NodeOutConnections (BaseModel):
    host = CharField()
    owner = CharField()
    join_at = DateTimeField(null=True)
    last_interaction = DateTimeField(null=True)

class NodeForbidenConnections (BaseModel):
        host = CharField()
        owner = CharField()
        forbiden_at = DateTimeField()

class Feeds(BaseModel):
    host = CharField()
    owner = CharField()
    recived_at = DateTimeField()
    body = JSONField()

def createInNodeConnection(host, owner):
    NodeInConnections.get_or_create(
        host = host,
        owner = owner,
        join_at = datetime.datetime.now(),
        last_interaction = datetime.datetime.now()

    )
def createForbidenNodeConnection(host, owner):
    NodeInConnections.get_or_create(
        host = host,
        owner = owner,
        forbiden_at = datetime.datetime.now()
    )
def createOutNodeConnection(host, owner):
    NodeOutConnections.get_or_create(
        host = host,
        owner = owner,
        join_at = datetime.datetime.now(),
        last_interaction = datetime.datetime.now()
    )

def getNodeInConnectionsList():
    return NodeInConnections.select().dicts().get()

def getNodeOutConnectionsList():
    return NodeOutConnections().select().dicts().get()

def getNodeForbidenConnectionsList():
    return NodeForbidenConnections().select().dicts().get()


def runMigrate():
    try:
        NodeInConnections.create_table()
        print("'NodeInConnections' storage created successfully!")
        NodeOutConnections.create_table()
        print("'NodeOutConnections' storage created successfully!")
        NodeForbidenConnections.create_table()
        print("'NodeForbidenConnections' storage created successfully!")
        Feeds.create_table()
        print("'Feeds' storage created successfully!")
    except OperationalError:
        print("'Some' storage already exists!")

