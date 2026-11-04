from pathlib import Path


path = Path("Python_Standard_Lib")

# path.exists() # returns a boolean
# path.mkdir() # to create in this directory
# path.rmdir() # to remove it
# path.rename("ecommerce2") # to rename

# path.iterdir() # get list of files and directories in this path

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
#[PosixPath('Python_Standard_Lib/paths.py'), PosixPath('Python_Standard_Lib/directories.py')]
# Two-Limitations of iterdir()
# 1. It cannot search by patterns
# 2. It doesn't search recursively

# Using glob() to skipped those limitations
py_files = [p for p in path.glob("*.py")]
# py_files = [p for p in path.glob("*.py")] # to search recursively
# py_files = [p for p in path.rglob("*.py")] # or use rglob(); recursive-glob
print(py_files)