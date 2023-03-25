
"""
Path Turning Addon module for FreeCAD.
This file is a standard FreeCAD Addon file
it exists to load the addon data.
"""
FC_MAJOR_VER_REQUIRED = 0
FC_MINOR_VER_REQUIRED = 19
FC_PATCH_VER_REQUIRED = 0
FC_COMMIT_REQUIRED = 24267
ver = FreeCAD.Version()
major_ver = int(ver[0])
minor_vers = ver[1].split('.')
minor_ver = int(minor_vers[0])
if minor_vers[1:] and minor_vers[1]:
    patch_ver = int(minor_vers[1])
else:
    patch_ver = 0
gitver = ver[2].split()
if gitver:
    gitver = gitver[0]
if gitver and gitver != 'Unknown':
    gitver = int(gitver)
else:
    # If we don't have the git version, assume it's OK.
    gitver = FC_COMMIT_REQUIRED
if (major_ver < FC_MAJOR_VER_REQUIRED or
    (major_ver == FC_MAJOR_VER_REQUIRED and
     (minor_ver < FC_MINOR_VER_REQUIRED or
      (minor_ver == FC_MINOR_VER_REQUIRED and
       (patch_ver < FC_PATCH_VER_REQUIRED or
        (patch_ver == FC_PATCH_VER_REQUIRED and
         gitver < FC_COMMIT_REQUIRED)))))):
    fc_msg = "Turning_Addon requires FreeCAD version {}.{}.{} ({})\n".format(
        FC_MAJOR_VER_REQUIRED, FC_MINOR_VER_REQUIRED, FC_PATCH_VER_REQUIRED, FC_COMMIT_REQUIRED)
    FreeCAD.Console.PrintError(fc_msg)
else:
    import InitTurningAddon  # noqa: F401
