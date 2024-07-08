import pathlib

import compas
from compas.geometry import Box

box = Box(1, 1, 1)
mesh = box.to_mesh().subdivided(k=4)

session = {"box": box, "mesh": mesh}
filepath = pathlib.Path(__file__).parent / "data" / "session.json"
compas.json_dump(session, filepath)
