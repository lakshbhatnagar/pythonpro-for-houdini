# importing houdini modules
import hou

# importing sys modules
import sys

# polygon sphere
def polySphere(path, name="polySphere", radius=1, rowsDivision=13, colsDivision=24):
    sphere = hou.node(path).createNode('sphere') # default houdini sphere
    sphere.setName(name) # sphere name
    sphere.parm("type").set("polymesh") # setting it's type to polyMesh
    sphere.parm("rows").set(rowsDivision) # rows division
    sphere.parm("cols").set(colsDivision) # columns division
    sphere.parm("scale").set(radius) # sphere radius

# polygon cube
def polyCube(path, name="polyCube", size=1, axisDivision=4):
    box = hou.node(path).createNode('box') # default houdini box
    box.setName(name) # box name
    box.parm("type").set("polymesh") # setting it's type to polyMesh
    box.parm("scale").set(size) # box scale
    box.parm("divrate1").set(axisDivision) # axis division 1
    box.parm("divrate2").set(axisDivision) # axis division 2
    box.parm("divrate3").set(axisDivision) # axis division 3

# polygon tube
def polyTube(path, name="polyTube", radius=1, height=1, rowsDivision=2, colsDivision=12):
    tube = hou.node(path).createNode('tube') # default houdini tube
    tube.setName(name) # tube name
    tube.parm("type").set("poly") # setting it's type to polygon
    tube.parm("radscale").set(radius) # tube radius
    tube.parm("height").set(height) # tube height
    tube.parm("rows").set(rowsDivision) # rows division
    tube.parm("cols").set(colsDivision) # columns division

# polygon torus
def polyTorus(path, name="polyTorus", radiusX=1, radiusY=0.5, scale=1, rowsDivision=12, colsDivision=24):
    torus = hou.node(path).createNode('torus')
    torus.setName(name) # torus name
    torus.parm("type").set("poly") # setting it's type to polygon
    torus.parm("radx").set(radiusX) # xRadius
    torus.parm("rady").set(radiusY) # yRadius
    torus.parm("scale").set(scale) # scale
    torus.parm("rows").set(rowsDivision) # rows division
    torus.parm("cols").set(colsDivision) # columns division
