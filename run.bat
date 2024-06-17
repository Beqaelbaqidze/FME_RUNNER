@echo off
REM Batch file to run Python script with ArcGIS Python interpreter
REM Author: B.K.

REM Define paths to ArcGIS Python interpreters
SET ARCGIS_DESKTOP_PYTHON="C:\Python27\ArcGIS10.1\python.exe"
SET ARCGIS_PRO_PYTHON="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

REM Define path to the Python script
SET SCRIPT_PATH="G:\for_fme\list_layers.py"

REM Set color for the command prompt
color 0A

REM Display header
echo ============================================================
echo =                   ArcGIS Python Script Runner            =
echo =                         Author: B.E.                     =
echo ============================================================

REM Check if ArcGIS Desktop Python interpreter exists
IF EXIST %ARCGIS_DESKTOP_PYTHON% (
    echo.
    echo [INFO] Running script with ArcGIS Desktop Python interpreter...
    %ARCGIS_DESKTOP_PYTHON% %SCRIPT_PATH%
    GOTO END
)

REM Check if ArcGIS Pro Python interpreter exists
IF EXIST %ARCGIS_PRO_PYTHON% (
    echo.
    echo [INFO] Running script with ArcGIS Pro Python interpreter...
    %ARCGIS_PRO_PYTHON% %SCRIPT_PATH%
    GOTO END
)

REM If neither interpreter is found
echo.
echo [ERROR] No ArcGIS Python interpreter found. Please check your installation.
GOTO END

:END
echo.
echo ============================================================
echo =                   Script execution finished.              =
echo ============================================================
pause
