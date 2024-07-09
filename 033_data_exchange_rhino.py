import compas
import pathlib
from compas.colors import Color
from compas.geometry import Box
from compas.scene import Scene

filepath = pathlib.Path(__file__).parent / "data" / "session.json"
session = compas.json_load(filepath)

box = session["box"]
mesh = session["mesh"]

scene = Scene()
scene.clear()
scene.add(box, color=Color.red())
scene.add(mesh, color=Color.green())
scene.draw()
