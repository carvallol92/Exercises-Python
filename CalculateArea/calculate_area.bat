@echo off
echo Fecha:%date%
echo Hora:%time%
color 0A
echo ===========================================
echo. 
echo          =   CALCULO DE AREA   =
echo. 
echo ===========================================
echo.
echo.
cd C:\test_python\ejercicios\python_platzi
"C:\Users\carva\AppData\Local\Programs\Python\Python37\python.exe" calculate_area.py

echo Fecha:%date%
echo Hora:%time%
PAUSE
echo.
echo.
echo Para salir presiona una tecla.
pause>nul
exit

