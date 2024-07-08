import rhinoscriptsyntax as rs  # noqa: I001  # type: ignore

import compas_rhino.objects
from compas.scene import Scene
from compas_fd.solvers import fd_numpy

# from compas_tna.diagrams import ForceDiagram
from compas_tna.diagrams import FormDiagram

# from compas_tna.equilibrium import horizontal_nodal
from compas_tna.equilibrium import vertical_from_zmax

# =============================================================================
# FormDiagram
# - from meshgrid
# - mark corners as supports
# - assign higher qs to the boundaries by default
# =============================================================================

form = FormDiagram.from_meshgrid(10, 10)

corners = form.vertices_where(vertex_degree=2)
form.vertices_attribute(name="is_support", value=True, keys=corners)

form.edges_attribute(name="q", value=10, keys=form.edges_on_boundary())

# =============================================================================
# Scene
# - clear everything (only do this if you really mean it)
# - draw the form diagram without faces
# =============================================================================

scene = Scene()
scene.clear()

formobj = scene.add(form, show_forces=False, show_faces=False)  # store the form diagram scene object

scene.draw()

# =============================================================================
# Numerical data
# - applied point loads
# - supports as fixed points
# - edge topology (remains constant)
# =============================================================================

loads = form.vertices_attributes(names=["px", "py", "pz"])
fixed = list(form.vertices_where(is_support=True))
edges = list(form.edges())

# =============================================================================
# Interactively update edge force densities
# - Get all edges on the same loop as a selected edge
# - Ask for a force density value
# - Compute horizontal equilibrium with compas_fd (more interesting things can be done with the constrained version)
# - Update vertical equilibrium
# - Update visualisation
# =============================================================================

while True:
    rs.UnselectAllObjects()  # without this, the previously selected edge is automatically selected again

    guid = compas_rhino.objects.select_curve("Select an edge of the diagram.")
    if not guid:
        break

    guid_edge = {guid: edge for guid, edge in zip(formobj._guids_edges, form.edges())}

    if guid in guid_edge:
        edge = guid_edge[guid]
        loop = form.edge_loop(edge)

        q = rs.GetReal("Force Density", minimum=0, maximum=1000)

        if q is not None:
            form.edges_attribute(name="q", value=q, keys=loop)

            vertices = form.vertices_attributes(names=["x", "y", "z"])  # use the current coordinates
            q = form.edges_attribute("q")  # use the current force densities

            result = fd_numpy(
                vertices=vertices,
                fixed=fixed,
                edges=edges,
                forcedensities=q,
                loads=loads,
            )

            for vertex, attr in form.vertices(data=True):
                # setting `data=True` returns a view of the vertex attribute data (`attr`)
                # together with the vertex identifier (`vertex`)
                # this data view is live and can be modified in place
                attr["x"] = result.vertices[vertex, 0]
                attr["y"] = result.vertices[vertex, 1]
                attr["z"] = result.vertices[vertex, 2]

            vertical_from_zmax(form, zmax=3)

            # this resets some of the cached values of the scene object
            # such that the visualisation is correct...
            formobj.diagram = form

            # redraw the scene
            scene.draw()

# =============================================================================
# Show the result as a mesh with faces
# =============================================================================

formobj.show_faces = True
formobj.show_edges = False

# =============================================================================
# Optional
# - Update the boundaries of the form diagram
# - Make a force diagram
# - Update the geometry of the force diagram
# =============================================================================

# form.update_boundaries()
# force = ForceDiagram.from_formdiagram(form)
# horizontal_nodal(form, force)

# scene.add(force, show_vertices=False, show_faces=False)

scene.draw()
