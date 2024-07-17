:: Deletes logs older than 14 days

@echo off
SET "directory=..\logs"
SET "days=14"
SET "count=0"

REM Deleting files older than specified days
forfiles /p "%directory%" /s /m *.* /d -%days% /c "cmd /c del @file && set /a count+=1"

echo %count% files older than %days% days in %directory% have been deleted.
pause