#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^y::pause ; Ctrl + Y to pause, after finding the lobby usually
!y:: ; Alt + Y to start the script.

Loop,
{
SendInput, m
Sleep, 3600000
}