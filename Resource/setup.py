from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Main.py", base=base), Executable("Home.py", base=base), Executable("process.py", base=base), Executable("Uiform.py", base=base), Executable("Db.py", base=base)]

packages = ["selenium", "urllib", "PyQt5", "os", "json", "sys","PyQt5.Qt"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Neobux Registration",
    options = options,
    version = "1.0",
    description = 'Registers you into Neobux',
    executables = executables
)

