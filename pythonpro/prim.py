# importing houdini modules
import hou

# importing sys modules
import sys

# polygon sphere
def polySphere(path, name, radius, subd):
    sphere = hou.node(path).createNode('sphere') # default houdini sphere
    sphere.setName(name) # sphere name
    sphere.parm("type").set("polymesh") # setting it's type to polyMesh
    sphere.parm("rows").set(subd) # rows division
    sphere.parm("cols").set(subd) # columns division
    sphere.parm("scale").set(radius) # sphere radius

# polygon cube
def polyCube(path, name, size, axisDivision):
    box = hou.node(path).createNode('box') # default houdini box
    box.setName(name) # box name
    box.parm("type").set("polymesh") # setting it's type to polyMesh
    box.parm("scale").set(size) # box scale
    box.parm("divrate1").set(axisDivision) # axis division 1
    box.parm("divrate2").set(axisDivision) # axis division 2
    box.parm("divrate3").set(axisDivision) # axis division 3

# polygon tube
def polyTube(path, name, radius, height, rowsDivision, colsDivision):
    tube = hou.node(path).createNode('tube') # default houdini tube
    tube.setName(name) # tube name
    tube.parm("type").set("poly") # setting it's type to polygon
    tube.parm("radscale").set(radius) # tube radius
    tube.parm("height").set(height) # tube height
    tube.parm("rows").set(rowsDivision) # rows division
    tube.parm("cols").set(colsDivision) # columns division
