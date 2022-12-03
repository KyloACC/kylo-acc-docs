#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^y:: ; CTRL + Y to start the script.

CockpitCam:
Send, {Down}
Sleep, 100
Send, {Left}
Sleep, 100
Send, {Enter}
Sleep, 100
Send, {Right}
Sleep, 100
Send, {Enter}
Sleep, 5000
SendInput, {Numpad1}

Sleep, 20000
SendInput, {Numpad2}
Send, {Down}
Sleep, 100
Send, {Enter}

ChaseCam:
Loop, 5
{
Send, {F1} ; 5x F1 to get to close chase cam
}
Send, {Down}
Sleep, 100
Send, {Left}
Sleep, 100
Loop, 5
{
Send, {Enter} ; 5x 5s back + 5s waiting for the timeline to disappear, to be at the exact spot we were before but in chase cam.
Sleep, 100
}
Send, {Right}
Sleep, 100
Send, {Enter}
Sleep, 5000
SendInput, {Numpad2}
Sleep, 20000
Send, {Numpad2}
Send, {Down}
Sleep, 100
Send, {Enter}


TopView:
Loop, 3
{
Send, {F6} ; 3x F6 to get to TopView (from ACC Drive)
}
Send, {Down}
Sleep, 100
Send, {Left}
Sleep, 100
Loop, 5
{
Send, {Enter} ; 5x 5s back + 5s waiting for the timeline to disappear, to be at the exact spot we were before but in chase cam.
Sleep, 100
}
Send, {Right}
Sleep, 100
Send, {Enter}
Sleep, 5000
SendInput, {Numpad2}
Sleep, 20000
Send, {Numpad2}
Send, {Down}
Sleep, 100
Send, {Enter}

SendInput, {Numpad1}

MsgBox, It is done.

return