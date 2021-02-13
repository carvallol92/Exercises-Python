@echo off
echo Date ini:%date%
echo Time ini:%time%
color 0B
echo ===========================================
echo. 
echo          =   Contact Book   =
echo. 
echo ===========================================
echo.
echo.
"C:\Program Files\Python39\python.exe" contact_book.py

echo Date end:%date%
echo Time end:%time%
PAUSE
echo.
echo.
echo Push any key to go out...
pause>nul
exit
