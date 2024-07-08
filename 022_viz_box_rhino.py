from compas.colors import Color
from compas.geometry import Box
from compas.scene import Scene

box = Box(8, 1, 1)

scene = Scene()
scene.clear()
scene.add(box, color=Color.red())
scene.draw()
