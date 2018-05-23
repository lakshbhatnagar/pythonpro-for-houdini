# importing houdini modules
import hou

# importing sys modules
import sys

# selected node
def selNodes():
    for sel in hou.selectedNodes():
        return sel

# selected items
def selItems():
    for sel in hou.selectedItems():
        return sel

# rename selected 
def renameSelected(name):
    # getting selected node
    for sel in hou.selectedNodes():
        pass 

    # assigning to path attr
    path = sel.path()

    # renaming object
    hou.node(path).setName(name)

# rename node
def renameNode(node, name):
    # getting node
    obj = hou.node(node)

    # assigning to path attr
    path = obj.path()

    # renaming object
    hou.node(path).setName(name)

def parameters(node, parameterName, value):
    # getting node
    userNode = hou.node(node)

    # adjusting parm value
    userNode.parm(parameterName).set(value)
