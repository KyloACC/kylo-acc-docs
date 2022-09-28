#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

ControlSend, {Numpad1}, ahk_exe obs64.exe
^y:: ; CTRL + Y to start the script.

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
ControlSend, {Numpad1}, ahk_exe obs64.exe

Sleep, 20000
Send, {Numpad2}
Send, {Down}
Sleep, 100
Send, {Enter}

Loop, 3
{
Send, {F6}
}
Send, {Down}
Sleep, 100
Send, {Left}
Sleep, 100
Loop, 5
{
Send, {Enter}
Sleep, 100
}
Send, {Right}
Sleep, 100
Send, {Enter}
Sleep, 5000
Send, {Numpad2}

Sleep, 20000
Send, {Numpad2}
Send, {Down}
Sleep, 100
Send, {Enter}

MsgBox, It is done.

return