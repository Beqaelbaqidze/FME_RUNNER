import subprocess
import os

# Define the directory where the scripts are located
script_dir = r"G:\FME_RUNNER"

# Define the full paths to the scripts
copy_gdb_script = os.path.join(script_dir, "copy_gdb.py")
process_93_gdb_script = os.path.join(script_dir, "process_93_gdb.py")

# Run the first script to copy and rename the 10.1 File Geodatabase
print("Running copy_gdb.py...")
subprocess.call(["python", copy_gdb_script])

# Run the second script to handle the 9.3 File Geodatabase operations
print("Running process_93_gdb.py...")
subprocess.call(["python", process_93_gdb_script])
