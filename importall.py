import os, glob, gdb

script_dir = os.path.dirname(__file__)
loader_name = os.path.basename(__file__)

# find python scripts in this folder and in immediate subfolders
script_paths = glob.glob(os.path.join(script_dir, "*.py")) + \
               glob.glob(os.path.join(script_dir, "*", "*.py"))

for path in script_paths:
    if os.path.basename(path) == loader_name:
        continue  # skip myself

    gdb.execute(f"source {path}")
    print(f"[gdb] Loaded {path}")
