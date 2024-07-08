import compas
from compas.colors import Color
from compas.datastructures import Mesh
from compas.geometry import Box
from compas_viewer import Viewer

filepath = "/Users/adellend/c2/UCL_workshop/data/session.json"
session = compas.json_load(filepath)

box: Box = session["box"]
mesh: Mesh = session["mesh"]

viewer = Viewer()
viewer.scene.clear()
viewer.scene.add(box, color=Color.red())
viewer.scene.add(mesh, color=Color.green())
viewer.show()
