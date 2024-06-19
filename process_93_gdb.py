import arcpy
import os
import time
from datetime import datetime

# Read the path to the copied 10.1 File Geodatabase from the text file
try:
    with open("copied_gdb_path.txt", "r") as file:
        gdb_10_1_copy = file.read().strip()
except IOError as e:
    print("Error reading copied_gdb_path.txt: {}".format(e))
    raise

# Get the current date and time, and format it to include AM/PM
current_time = datetime.now().strftime("%Y-%m-%d_%I-%M_%p")

# Define the directory and the name for the new 9.3 File Geodatabase
gdb_9_3_dir = r"G:\for_fme"
gdb_9_3_name = "{}_93.gdb".format(current_time)
gdb_9_3 = os.path.join(gdb_9_3_dir, gdb_9_3_name)

def wait_for_copy_completion(gdb_path, timeout=300, interval=10):
    start_time = time.time()
    while not arcpy.Exists(gdb_path):
        if time.time() - start_time > timeout:
            raise Exception("Timeout waiting for {} to be created.".format(gdb_path))
        time.sleep(interval)
    print("{} exists. Waiting for copy operation to stabilize.".format(gdb_path))
    time.sleep(interval)

try:
    # Verify arcpy is working
    arcpy.GetInstallInfo()

    # Wait for the copy to complete
    wait_for_copy_completion(gdb_10_1_copy)
    
    # Check if the 9.3 File Geodatabase exists, if not, create it
    if not arcpy.Exists(gdb_9_3):
        arcpy.CreateFileGDB_management(gdb_9_3_dir, gdb_9_3_name, "9.3")
        print("Created File Geodatabase at {}".format(gdb_9_3))
    
    # Set the workspace to the copied 10.1 File Geodatabase
    arcpy.env.workspace = gdb_10_1_copy
    
    # List all feature datasets in the copied 10.1 File Geodatabase
    datasets = arcpy.ListDatasets("", "Feature")
    
    # Copy each feature dataset
    if datasets:
        for dataset in datasets:
            in_dataset = os.path.join(gdb_10_1_copy, dataset)
            out_dataset = os.path.join(gdb_9_3, dataset)
            arcpy.Copy_management(in_dataset, out_dataset)
            print("Copied dataset {} to {}".format(in_dataset, out_dataset))
    
    # List all feature classes in the copied 10.1 File Geodatabase not in any dataset
    feature_classes = arcpy.ListFeatureClasses()
    
    if not feature_classes and not datasets:
        print("No feature classes or datasets found in {}".format(gdb_10_1_copy))
    else:
        # Copy each feature class to the 9.3 File Geodatabase
        for fc in feature_classes:
            in_fc = os.path.join(gdb_10_1_copy, fc)
            out_fc = os.path.join(gdb_9_3, fc)
            arcpy.CopyFeatures_management(in_fc, out_fc)
            print("Copied {} to {}".format(in_fc, out_fc))
    
    print("All layers and datasets copied successfully.")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
except AttributeError as e:
    print("AttributeError: {}".format(e))
    print("Ensure that the arcpy module is correctly installed and accessible.")
except Exception as e:
    print("An error occurred: {}".format(e))
