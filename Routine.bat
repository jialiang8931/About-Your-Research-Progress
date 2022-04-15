@echo off 

D:
cd "D:\Yes"

if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin

start /min install.bat

timeout /t 2

start /min python CreateFig.py
start .\sample-out.jpg

exit