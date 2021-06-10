import os
import glob
import sys
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

python_exec=sys.executable

kiConfigPath = input("KICAD Config folder: ")

if not os.path.exists(kiConfigPath):
    print(bcolors.FAIL + "Ruta invalida." + bcolors.ENDC)
    exit(1)
    
def copyPlugin(src, dest):
    print(bcolors.WARNING + "-> " + bcolors.OKGREEN + "cp " + bcolors.WARNING + os.path.normpath(src) + " " + os.path.normpath(dest) + bcolors.ENDC)
    shutil.copytree(os.path.normpath(src), os.path.normpath(dest), dirs_exist_ok=True)

#---------------------------------------------------
#                 KICAD Color Scheme SETUP
#---------------------------------------------------
print(bcolors.HEADER + "Available Color Schemes: " + bcolors.ENDC)
colorSchemesPaths=glob.glob("./color-schemes/*/")
colorSchemesNames=colorSchemesPaths
colorSchemesNames = list(map(lambda x: os.path.basename(os.path.normpath(x)),colorSchemesNames))

i=0
for t in colorSchemesNames:
    print(" " + bcolors.BOLD + str(i) + bcolors.WARNING + ": " + bcolors.OKCYAN + t + bcolors.ENDC)
    i += 1
colorSchemeNumber = input(bcolors.HEADER + "Select a colorScheme (number): " + bcolors.ENDC)

colorScheme = os.path.normpath(colorSchemesPaths[int(colorSchemeNumber)])
colorSchemeName = colorSchemesNames[int(colorSchemeNumber)]
if not os.path.exists(colorScheme):
    print(bcolors.FAIL + "Nombre invalido." + bcolors.ENDC)
    exit(1)

print(bcolors.HEADER + "Tema seleccionado: " + bcolors.OKCYAN + colorSchemeName + bcolors.ENDC)



#---------------------------------------------------
#                 KICAD Color Scheme INSTALL
#---------------------------------------------------
print(bcolors.HEADER + "Installing KiCad Color Scheme: " + colorSchemeName + bcolors.ENDC)
print(bcolors.WARNING + "-> " + bcolors.OKGREEN + python_exec + bcolors.WARNING + " " + os.path.normpath("./color-schemes/patch.py") + " " + colorScheme + " " + os.path.normpath(kiConfigPath) + bcolors.ENDC)

os.system(python_exec + " ./color-schemes/patch.py " + colorScheme + " " + os.path.normpath(kiConfigPath))
print(bcolors.OKGREEN + "done." + bcolors.ENDC)

#---------------------------------------------------
#          KICAD InteractiveHtmlBom INSTALL
#---------------------------------------------------
print(bcolors.HEADER + "Installing KiCad InteractiveHtmlBom" + bcolors.ENDC)
copyPlugin("./interactive-html-bom/InteractiveHtmlBom", kiConfigPath + "/scripting/plugins/InteractiveHtmlBom")
print(bcolors.OKGREEN + "done." + bcolors.ENDC)


#---------------------------------------------------
#               KICAD RF-tools INSTALL
#---------------------------------------------------
print(bcolors.HEADER + "Installing KiCad RF-tools" + bcolors.ENDC)
copyPlugin("./RF-tools-KiCAD/rf_tools_wizards", kiConfigPath + "/scripting/plugins/rf_tools_wizards")
copyPlugin("./RF-tools-KiCAD/round_tracks", kiConfigPath + "/scripting/plugins/round_tracks")
copyPlugin("./RF-tools-KiCAD/trace_clearance", kiConfigPath + "/scripting/plugins/trace_clearance")
copyPlugin("./RF-tools-KiCAD/trace_solder_expander", kiConfigPath + "/scripting/plugins/trace_solder_expander")
copyPlugin("./RF-tools-KiCAD/tracks_length", kiConfigPath + "/scripting/plugins/tracks_length")
copyPlugin("./RF-tools-KiCAD/via_fence_generator", kiConfigPath + "/scripting/plugins/via_fence_generator")
print(bcolors.OKGREEN + "done." + bcolors.ENDC)


#---------------------------------------------------
#          KICAD Teardrops INSTALL
#---------------------------------------------------
print(bcolors.HEADER + "Installing KiCad Teardrops" + bcolors.ENDC)
copyPlugin("./teardrops/teardrops", kiConfigPath + "/scripting/plugins/teardrops")
print(bcolors.OKGREEN + "done." + bcolors.ENDC)


#---------------------------------------------------
#          KICAD Diff INSTALL
#---------------------------------------------------
print(bcolors.HEADER + "Installing KiCad Diff" + bcolors.ENDC)
copyPlugin("./diff", kiConfigPath + "/tools/diff")
print("Add folder to system PATH: " + os.path.normpath(kiConfigPath + "/tools/diff") + bcolors.ENDC)
print(bcolors.OKGREEN + "done." + bcolors.ENDC)

os.environ["PATH"] += os.pathsep + os.path.normpath(kiConfigPath + "/tools/diff")

print(bcolors.OKGREEN + "Everything done." + bcolors.ENDC)
exit(0)