import compas
import compas_rhino.objects
import compas_rhino.conversions

guid = compas_rhino.objects.select_mesh()
rmesh = compas_rhino.objects.find_object(guid)
mesh = compas_rhino.conversions.mesh_to_compas(rmesh)

filepath = pathlib.Path(__file__).parent / "data" / "mesh.json"
compas.json_dump(mesh, filepath)
