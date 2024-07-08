import pathlib

import compas
from compas.colors import Color
from compas.datastructures import Mesh
from compas_viewer import Viewer

# ==============================================================================
# Define the data files
# ==============================================================================

here = pathlib.Path(__file__).parent
cablemeshpath = here / "data" / "CableMesh.json"
sessionpath = here / "data" / "session.json"

# ==============================================================================
# Load the cablemesh
# ==============================================================================

cablemesh: Mesh = compas.json_load(cablemeshpath)

for vertex in cablemesh.vertices():
    cablemesh.unset_vertex_attribute(vertex, "constraint")

# ==============================================================================
# Define and export a work session
# ==============================================================================

session = {
    "cablemesh": cablemesh,
    "params": {
        "thickness": 0.15,
        "ribs": 0.05,
        "shell": 0.05,
    },
}

compas.json_dump(session, sessionpath)

# ==============================================================================
# Viz
# ==============================================================================

viewer = Viewer()

viewer.renderer.camera.target = [0, 0, 2]
viewer.renderer.camera.position = [3, -7, 3]

viewer.scene.add(cablemesh, color=Color.red())

viewer.show()
