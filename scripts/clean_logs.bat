:: Deletes logs older than 14 days

@echo off
SET "directory=../logs"
SET "days=14"

REM Deleting files older than specified days
forfiles /p "%directory%" /s /m *.* /d -%days% /c "cmd /c del @file"

echo Files older than %days% days in %directory% have been deleted.
pause