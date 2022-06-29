import json

from modules.database import (getNodeForbidenConnectionsList,
                              getNodeInConnectionsList,
                              getNodeOutConnectionsList)


def getNodeInList():
   try:
      list = getNodeInConnectionsList()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

def getNodeOutList():
   try:
      list = getNodeOutConnectionsList()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

def getNodeForbidenList():
   try:
      list = getNodeForbidenConnectionsList()
      return json.dumps(list, indent=4, sort_keys=True, default=str)
   except:
      return json.dumps({}, indent=4, sort_keys=True, default=str)

