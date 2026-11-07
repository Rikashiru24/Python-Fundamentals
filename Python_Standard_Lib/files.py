

from pathlib import Path
from time import ctime

path = Path("Python_Standard_Lib/__init__.py")

# path.exists()
# path.rename("init.txt")
# path.unlink() # to delete it


print(path.stat()) # return info about the file
# os.stat_result(st_mode=33188, st_ino=147731726, st_dev=16777230, st_nlink=1, st_uid=501, st_gid=20, st_size=0, st_atime=1794019761, st_mtime=1794019761, st_ctime=1794019761)


print(ctime(path.stat().st_ctime)) 
# Sat Nov  7 10:49:21 2026