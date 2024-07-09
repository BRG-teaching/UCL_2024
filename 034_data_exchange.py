import compas
import pathlib
from compas.colors import Color
from compas.datastructures import Mesh
from compas.geometry import Box
from compas_viewer import Viewer

filepath = pathlib.Path(__file__).parent / "data" / "session.json"
session = compas.json_load(filepath)

box: Box = session["box"]
mesh: Mesh = session["mesh"]

viewer = Viewer()
viewer.scene.add(box, color=Color.red())
viewer.scene.add(mesh, color=Color.green())
viewer.show()
