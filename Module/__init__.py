import os

EXEPTION_FILES = [
    "__init__.py",
    "__pycache__"
]

path_list = os.listdir(os.path.dirname(__file__))
for path in path_list:
    filename = os.path.basename(path)
    if filename in EXEPTION_FILES:
        continue
    basename = os.path.splitext(filename)[0]
    exec(f"from .{basename} import *")
