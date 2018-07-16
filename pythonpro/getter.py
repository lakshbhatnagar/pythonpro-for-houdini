# importing houdini modules
import hou

# selected node
def getSelectedNodes():
    for sel in hou.selectedNodes():
        return sel

# selected items
def getSelectedItems():
    for sel in hou.selectedItems():
        return sel

# getting selected node path
def getSelectedNodePath():
    # getting selected object
    for sel in hou.selectedNodes():
        pass

    # extracting path from selected object
    path = sel.path()
    return path

# getting selected node parent path
def getSelectedNodeParentPath():
    # getting selected object
    for sel in hou.selectedNodes():
        pass

    # store selected object parent
    obj = sel.parent()

    # extracting path from selected object
    path = obj.path()
    return path

