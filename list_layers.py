import arcpy
import os
from datetime import datetime

# Define the path to the 10.1 File Geodatabase
gdb_10_1 = r"G:\for_fme\output.gdb"

# Get the current date and time, and format it to include AM/PM
current_time = datetime.now().strftime("%Y-%m-%d_%I-%M_%p")

# Define the directory and the name for the new 9.3 File Geodatabase
gdb_9_3_dir = r"G:\for_fme"
gdb_9_3_name = "{}_93.gdb".format(current_time)
gdb_9_3 = os.path.join(gdb_9_3_dir, gdb_9_3_name)

# Define the path for the new copy of the 10.1 File Geodatabase
gdb_10_1_copy_name = "{}_10.gdb".format(current_time)
gdb_10_1_copy = os.path.join(gdb_9_3_dir, gdb_10_1_copy_name)

try:
    # Verify arcpy is working
    arcpy.GetInstallInfo()
    
    # Function to copy and rename the 10.1 File Geodatabase
    def copy_and_rename_gdb(source_gdb, destination_gdb):
        if arcpy.Exists(source_gdb):
            arcpy.Copy_management(source_gdb, destination_gdb)
            print("Copied and renamed File Geodatabase from {} to {}".format(source_gdb, destination_gdb))
        else:
            print("Source File Geodatabase {} does not exist.".format(source_gdb))
    
    # Call the function to copy and rename the 10.1 File Geodatabase
    copy_and_rename_gdb(gdb_10_1, gdb_10_1_copy)
    
    # Check if the 9.3 File Geodatabase exists, if not, create it
    if not arcpy.Exists(gdb_9_3):
        arcpy.CreateFileGDB_management(gdb_9_3_dir, gdb_9_3_name, "9.3")
        print("Created File Geodatabase at {}".format(gdb_9_3))
    
    # List all feature datasets in the 10.1 File Geodatabase
    arcpy.env.workspace = gdb_10_1
    datasets = arcpy.ListDatasets("", "Feature")
    
    # Copy each feature dataset
    if datasets:
        for dataset in datasets:
            in_dataset = os.path.join(gdb_10_1, dataset)
            out_dataset = os.path.join(gdb_9_3, dataset)
            arcpy.Copy_management(in_dataset, out_dataset)
            print("Copied dataset {} to {}".format(in_dataset, out_dataset))
    
    # List all feature classes in the 10.1 File Geodatabase not in any dataset
    feature_classes = arcpy.ListFeatureClasses()
    
    if not feature_classes and not datasets:
        print("No feature classes or datasets found in {}".format(gdb_10_1))
    else:
        # Copy each feature class to the 9.3 File Geodatabase
        for fc in feature_classes:
            in_fc = os.path.join(gdb_10_1, fc)
            out_fc = os.path.join(gdb_9_3, fc)
            arcpy.CopyFeatures_management(in_fc, out_fc)
            print("Copied {} to {}".format(in_fc, out_fc))
    
    print("All layers and datasets copied successfully.")
except AttributeError as e:
    print("AttributeError: {}".format(e))
    print("Ensure that the arcpy module is correctly installed and accessible.")
except Exception as e:
    print("An error occurred: {}".format(e))
