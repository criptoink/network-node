import json

from shared.modules.database import (get_node_forbidden_connections_list,
                                     get_node_in_connections_list,
                                     get_node_out_connections_list)


def get_node_in_list():
   try:
      list = get_node_in_connections_list()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

def get_node_out_list():
   try:
      list = get_node_out_connections_list()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

def get_node_forbidden_list():
   try:
      list = get_node_forbidden_connections_list()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

