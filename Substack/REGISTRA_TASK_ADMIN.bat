@echo off
:: ============================================================
:: INNESCO — Registrazione Task Scheduler
:: Esegui questo file con TASTO DESTRO → "Esegui come amministratore"
:: ============================================================

echo.
echo  ================================================
echo   INNESCO - Registrazione Task Automatico
echo  ================================================
echo.
echo  Registro il task per la generazione automatica
echo  dei post Substack ogni mattina alle 07:00...
echo.

powershell.exe -ExecutionPolicy Bypass -Command ^
  "$scriptPath = 'C:\Users\Domenico\Desktop\cartella per claude code\Utilità\magazine di dome\Substack\genera_post_substack.ps1'; ^
   $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument ('-ExecutionPolicy Bypass -WindowStyle Hidden -NonInteractive -File \"' + $scriptPath + '\"'); ^
   $trigger = New-ScheduledTaskTrigger -Daily -At '07:00' -DaysInterval 1; ^
   $trigger.EndBoundary = '2026-05-16T00:00:00'; ^
   $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1) -MultipleInstances IgnoreNew -StartWhenAvailable; ^
   $task = Register-ScheduledTask -TaskName 'Innesco - Genera Post Substack' -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest -Force; ^
   Write-Host ('Task registrato: ' + $task.TaskName); ^
   Write-Host ('Prossima esecuzione: ' + $task.NextRunTime)"

if %ERRORLEVEL% EQU 0 (
  echo.
  echo  ================================================
  echo   SUCCESSO! Task registrato correttamente.
  echo.
  echo   Il post verra' generato ogni mattina alle 7:00
  echo   dal 9 maggio al 15 maggio 2026.
  echo.
  echo   Puoi verificarlo aprendo:
  echo   Utilità Windows → Utilità di pianificazione →
  echo   Libreria → "Innesco - Genera Post Substack"
  echo  ================================================
) else (
  echo.
  echo  ERRORE durante la registrazione.
  echo  Assicurati di aver cliccato con TASTO DESTRO
  echo  e scelto "Esegui come amministratore".
)

echo.
pause
