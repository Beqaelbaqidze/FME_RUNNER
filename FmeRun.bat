@echo off
REM Set the path to the FME executable
set FME_EXE="C:\Program Files\FME\fme.exe"

REM Set the path to your FME workspace file
set FME_WORKSPACE="G:\FME_RUNNER\FME_PROJ\REDI_INFO.fmw"

REM Set the source and destination datasets
set SOURCE_DATASET="TBILREG"
set DEST_DATASET="G:\for_fme\output.gdb"

REM Run the FME workspace with the specified parameters
%FME_EXE% %FME_WORKSPACE% --SourceDataset_ORACLE_SPATIAL %SOURCE_DATASET% --DestDataset_FILEGDB %DEST_DATASET% --OverwriteExistingDatasets "YES" --FME_LAUNCH_VIEWER_APP "YES"

REM Run the second batch file after completion
call "G:\FME_RUNNER\run_python_scripts.bat"
