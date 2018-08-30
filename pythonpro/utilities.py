# importing houdini modules
import hou
import os

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

# import latest setup files

def importSetup():
    ask = hou.ui.readInput("Enter Element Name") [1]
    pathDir = hou.ui.readInput("Enter Path") [1] 
    listDir = os.listdir(pathDir)
    sortedDir = sorted(listDir)
    length = len(sortedDir)

    i = 0
    while i < length:
        if(sortedDir[i].find(ask) == 12):
            MyList = []
            MyList.append(sortedDir[i])
        else:
            pass
        i += 1
        pass

    houdiniSceneFile = pathDir + "/" + MyList[0] + "/" + "script" + "/" + MyList[0] + ".hip"
    hou.hipFile.merge(houdiniSceneFile)
    return houdiniSceneFile

