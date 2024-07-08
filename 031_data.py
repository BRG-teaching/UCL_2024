import pathlib

import compas
from compas.geometry import Box

box = Box(1, 1, 1)
mesh = box.to_mesh().subdivided(k=4)

filepath = pathlib.Path(__file__).parent / "data" / "mesh.json"
compas.json_dump(box, filepath)
