import compas
import compas_rhino.objects
import compas_rhino.conversions
import pathlib


# =============================================================================
# mesh from rhino
# =============================================================================
guid = compas_rhino.objects.select_mesh()
mesh = compas_rhino.conversions.meshobject_to_compas(guid)

# =============================================================================
# lines from rhino
# =============================================================================
guids = compas_rhino.objects.select_lines()
objects = [compas_rhino.objects.find_object(guid) for guid in guids]
lines = [compas_rhino.conversions.curve_to_compas_line(obj.Geometry) for obj in objects]

# =============================================================================
# brep from rhino
# =============================================================================
guid = compas_rhino.objects.select_surface()
surface = compas_rhino.conversions.brepobject_to_compas(guid)

# =============================================================================
# to json
# =============================================================================
filepath = pathlib.Path(__file__).parent / "data" / "mesh_rhino.json"
compas.json_dump(mesh, filepath)
