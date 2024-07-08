import pathlib

import compas
from compas.geometry import Box

box = Box(1, 1, 1)

filepath = pathlib.Path(__file__).parent / "data" / "box.json"
compas.json_dump(box, filepath)
