 # importing houdini modules
import hou

# display flag
def setDisplayFlag(node, on):
    # getting node
    obj = hou.node(node)

    # set display flag
    obj.setDisplayFlag(on)

    # return
    if(on==True):
        return True
    else:
        return False

# rename selected 
def setSelectedName(name):
    # getting selected node
    for sel in hou.selectedNodes():
        pass 

    # assigning to path attr
    path = sel.path()

    # renaming object
    hou.node(path).setName(name)

# rename node
def setNodeName(node, name):
    # getting node
    obj = hou.node(node)

    # assigning to path attr
    path = obj.path()

    # renaming object
    hou.node(path).setName(name)

# set parameters
def setParameters(node, parameterName, value):
    # getting node
    userNode = hou.node(node)

    # adjusting parm value
    userNode.parm(parameterName).set(value)

# push button
def setPushButton(node, buttonName):
    # getting node
    obj = hou.node(node)

    # push button
    obj.parm(buttonName).pressButton()
