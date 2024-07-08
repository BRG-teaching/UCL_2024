import compas
import compas_dr
import compas_fd
import compas_tna
import compas_occ
import compas_viewer


def check_version(package, version):
    return f"{version} => {package.__version__}  {'OK' if package.__version__ == version else 'ERROR'}"


print(f"compas          : {check_version(compas, '2.3.0')}")
print(f"compas_dr       : {check_version(compas_dr, '0.3.1')}")
print(f"compas_fd       : {check_version(compas_fd, '0.5.1')}")
print(f"compas_tna     : {check_version(compas_tna, '0.4.0')}")
print(f"compas_occ      : {check_version(compas_occ, '1.2.0')}")
print(f"compas_viewer   : {check_version(compas_viewer, '1.2.3')}")
