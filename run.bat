@echo off
REM 设置控制台编码为 UTF-8
chcp 65001 >nul

echo Current directory: %cd%
py --version

SET PYTHON_EXEC=py

%PYTHON_EXEC% dc.py
IF %ERRORLEVEL% NEQ 0 (
    ECHO "dc.py 执行失败"
    PAUSE
    EXIT /B %ERRORLEVEL%
)

ECHO "dc.py 执行完毕"
PAUSE