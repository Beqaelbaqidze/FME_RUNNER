@echo off
REM Batch file to run Python script with ArcGIS Python interpreter
REM Author: B.K.

REM Define paths to ArcGIS Python interpreters
SET ARCGIS_DESKTOP_PYTHON="C:\Python27\ArcGIS10.1\python.exe"
SET ARCGIS_PRO_PYTHON="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

REM Define the directory containing the Python scripts
SET SCRIPT_DIR="G:\FME_RUNNER"

REM Define path to the Python scripts
SET MAIN_SCRIPT_PATH="%SCRIPT_DIR%\main_script.py"
SET COPY_SCRIPT_PATH="%SCRIPT_DIR%\copy_gdb.py"
SET PROCESS_SCRIPT_PATH="%SCRIPT_DIR%\process_93_gdb.py"

REM Define log file path
SET LOG_FILE="%SCRIPT_DIR%\script_log.txt"

REM Set color for the command prompt
color 0A

REM Display header
echo ============================================================ > %LOG_FILE%
echo =                   ArcGIS Python Script Runner            = >> %LOG_FILE%
echo =                         Author: B.K.                     = >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%

REM Check if ArcGIS Desktop Python interpreter exists
IF EXIST %ARCGIS_DESKTOP_PYTHON% (
    echo. >> %LOG_FILE%
    echo [INFO] Running main script with ArcGIS Desktop Python interpreter... >> %LOG_FILE%
    cd /d %SCRIPT_DIR%
    %ARCGIS_DESKTOP_PYTHON% %MAIN_SCRIPT_PATH% >> %LOG_FILE% 2>&1
    GOTO END
)

REM Check if ArcGIS Pro Python interpreter exists
IF EXIST %ARCGIS_PRO_PYTHON% (
    echo. >> %LOG_FILE%
    echo [INFO] Running main script with ArcGIS Pro Python interpreter... >> %LOG_FILE%
    cd /d %SCRIPT_DIR%
    %ARCGIS_PRO_PYTHON% %MAIN_SCRIPT_PATH% >> %LOG_FILE% 2>&1
    GOTO END
)

REM If neither interpreter is found
echo. >> %LOG_FILE%
echo [ERROR] No ArcGIS Python interpreter found. Please check your installation. >> %LOG_FILE%
GOTO END

:END
echo. >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%
echo =                   Script execution finished.              = >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%
