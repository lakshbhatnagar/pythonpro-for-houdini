# importing houdini modules
import hou

# merge selected objects
def mergeSelectedNodes():
    # storing selected nodes in a list
    sel = hou.selectedNodes()

    # extracting selected node parent path
    for i in hou.selectedNodes():
        pass

    parent = i.parent()    
    path = parent.path()

    # creating merge node
    createMergeNode = hou.node(path).createNode("merge")

    # set node parent
    for selNodes in sel:
        hou.Node.setNextInput(createMergeNode, selNodes)

    return createMergeNode
