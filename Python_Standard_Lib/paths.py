# Path Class


from pathlib import Path

# Path(r"C:\Program Files\Microsoft") # Windows
# Path("/usr/local/bin") # Mac
# Path()
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("ecommerce/__init__.py")
path.exists() # to check if this directory exists or not
path.is_file() # to check if represents a file
path.is_dir()
print(path.name) # return a file that it have
print(path.stem) # return file without extension
print(path.suffix) # to get the file extension ex: .py
print(path.parent) # to get the parent folder of that path
# path = path.with_name("file.txt") # Assign the returned new path back to a variable
path = path.with_suffix(".txt") # Assign the returned new path back to a variable; ecommerce/__init__.txt
print(path)


