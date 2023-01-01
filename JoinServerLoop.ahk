#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
CoordMode, Mouse, Screen

^y::pause ; Ctrl + Y to pause, after finding the lobby usually
!y:: ; Alt + Y to start the script.

Loop,
{
MouseClick, left, 1900, 250 ; Set for 2560x1440, use AutoHotkey Window Spy "Window" to find your coordinates
Sleep, 15000 ; 20s sleep after joining lobby to see weather

MouseClick, left, 1100, 240 ; Quit
Sleep, 500
MouseClick, left, 1075, 820 ; Confirm

Sleep, 7500 ; load servers
}


return