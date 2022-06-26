import datetime

from peewee import *
from playhouse.sqlcipher_ext import *
from playhouse.sqlite_ext import *

db = SqlCipherDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class NodeConnections(BaseModel):
    host = CharField()
    owner = CharField()
    join_at = DateTimeField(default=datetime.datetime.now)

class Feeds(BaseModel):
    host = CharField()
    owner = CharField()
    recived_at = DateTimeField()
    body = JSONField()

def createNodeConnection(host, owner):
    NodeConnections.get_or_create(
        host = host,
        owner = owner
    )
def connectGenesisNode():    
    createNodeConnection(
        'genesis.cripto.ink',
        '1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU'
    )
def getNodesList():
    return NodeConnections.select()

