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
def polyTorus(path, name, radius, height, rowsDivision, colsDivision):
    torus = hou.node(path).createNode('tube') # default houdini tube
    torus.setName(name) # torus name
    torus.parm("type").set("poly") # setting it's type to polygon
    torus.parm("radscale").set(radius) # torus radius
    torus.parm("height").set(height) # torus height
    torus.parm("rows").set(rowsDivision) # rows division
    torus.parm("cols").set(colsDivision) # columns division
