import shutil
import os
from datetime import datetime

# Define the path to the 10.1 File Geodatabase
gdb_10_1 = r"G:\for_fme\output.gdb"

# Get the current date and time, and format it to include AM/PM
current_time = datetime.now().strftime("%Y-%m-%d_%I-%M_%p")

# Define the directory and the name for the new 10.1 File Geodatabase copy
gdb_10_1_copy_dir = r"G:\for_fme"
gdb_10_1_copy_name = "{}_10.gdb".format(current_time)
gdb_10_1_copy = os.path.join(gdb_10_1_copy_dir, gdb_10_1_copy_name)

def ignore_lock_files(directory, files):
    """Ignore lock files during copy."""
    return [f for f in files if f.endswith('.lock')]

try:
    # Function to copy and rename the 10.1 File Geodatabase
    def copy_and_rename_gdb(source_gdb, destination_gdb):
        if os.path.exists(source_gdb):
            if os.path.exists(destination_gdb):
                print("Destination File Geodatabase {} already exists. Deleting it.".format(destination_gdb))
                shutil.rmtree(destination_gdb)
            print("Starting copy from {} to {}".format(source_gdb, destination_gdb))
            shutil.copytree(source_gdb, destination_gdb, ignore=ignore_lock_files)
            print("Copied and renamed File Geodatabase from {} to {}".format(source_gdb, destination_gdb))
        else:
            print("Source File Geodatabase {} does not exist.".format(source_gdb))
    
    # Call the function to copy and rename the 10.1 File Geodatabase
    copy_and_rename_gdb(gdb_10_1, gdb_10_1_copy)
    
    # Save the copied GDB path to a text file for later use
    with open("copied_gdb_path.txt", "w") as file:
        file.write(gdb_10_1_copy)
    
    print("GDB copy completed and path saved.")
except Exception as e:
    print("An error occurred: {}".format(e))
