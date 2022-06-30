import datetime

from peewee import *
from playhouse.sqlcipher_ext import *
from playhouse.sqlite_ext import *

db = SqlCipherDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class NodeInConnections(BaseModel):
    host = CharField()
    owner = CharField()
    join_at = DateTimeField(null=True)
    last_interaction = DateTimeField(null=True)


class NodeOutConnections(BaseModel):
    host = CharField()
    owner = CharField()
    join_at = DateTimeField(null=True)
    last_interaction = DateTimeField(null=True)


class NodeForbiddenConnections(BaseModel):
    host = CharField()
    owner = CharField()
    forbidden_at = DateTimeField()


class Feeds(BaseModel):
    host = CharField()
    owner = CharField()
    recived_at = DateTimeField()
    body = JSONField()


def create_node_in_connection(host, owner):
    NodeInConnections.get_or_create(
        host=host,
        owner=owner,
        join_at=datetime.datetime.now(),
        last_interaction=datetime.datetime.now()

    )


def create_node_forbidden_connection(host, owner):
    NodeInConnections.get_or_create(
        host=host,
        owner=owner,
        forbidden_at=datetime.datetime.now(),
        last_interaction = datetime.datetime.now()
    )


def create_node_out_connection(host, owner):
    NodeOutConnections.get_or_create(
        host=host,
        owner=owner,
        join_at=datetime.datetime.now(),
        last_interaction=datetime.datetime.now()
    )


def get_node_in_connections_list():
    return NodeInConnections.select().dicts().get()


def get_node_out_connections_list():
    return NodeOutConnections().select().dicts().get()


def get_node_forbidden_connections_list():
    return NodeForbiddenConnections().select().dicts().get()


def run_migrate():
    try:
        NodeInConnections.create_table()
        print("'NodeInConnections' storage created successfully!")
        NodeOutConnections.create_table()
        print("'NodeOutConnections' storage created successfully!")
        NodeForbiddenConnections.create_table()
        print("'NodeForbiddenConnections' storage created successfully!")
        Feeds.create_table()
        print("'Feeds' storage created successfully!")
    except OperationalError:
        print("'Some' storage already exists!")
