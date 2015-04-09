@ECHO OFF

REM Command file for the Python project

if "%PYTHON%" == "" (
	set PYTHON=python
)
if "%DISTDIR%" == "" (
	set DISTDIR=dist
)
if "%EGGDIR%" == "" (
	set EGGDIR=CWR_API.egg-info
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  sdist      to make the source distribution
	echo.  bdist      to make the binary distribution
	goto end
)

if "%1" == "clean" (
	if exist %DISTDIR% (
		rd /S /Q %DISTDIR%
	)
	if exist %EGGDIR% (
		rd /S /Q %EGGDIR%
	)
	goto end
)


REM Check if the interpreter is available
%PYTHON% -V> nul
if errorlevel 9009 goto missing_interpreter
goto interpreter_ok

:missing_interpreter

echo.
echo.The '%PYTHON%' command was not found. Make sure you have a
echo.version of the python interpreter installed, then add the
echo.directory where it was installed to the PATH.
echo.
exit /b 1

:interpreter_ok


if "%1" == "sdist" (
	echo %PYTHON% sdist
	if errorlevel 1 exit /b 1
	echo.
	echo.Generated source distribution. It can be found in the
	echo.%DISTDIR% folder.
	goto end
)

if "%1" == "bdist" (
	echo %PYTHON% bdist
	if errorlevel 1 exit /b 1
	echo.
	echo.Generated binary distribution. It can be found in the
	echo.%DISTDIR% folder.
	goto end
)

:end
