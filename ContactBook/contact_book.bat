@echo off
echo Fecha:%date%
echo Hora:%time%
color 0B
echo ===========================================
echo. 
echo          =   Contact Book   =
echo. 
echo ===========================================
echo.
echo.
cd C:\onedrive\test_python\python_platzi\directorio
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" contact_book.py

echo Fecha:%date%
echo Hora:%time%
PAUSE
echo.
echo.
echo Para salir presiona una tecla.
pause>nul
exit

