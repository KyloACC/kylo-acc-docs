#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
CoordMode, Mouse, Screen

^y::pause ; Ctrl + Y to pause, after finding the lobby usually
!x::reload ; Alt + X to reload script, to get back to the beginning.
; ALT + Y to start, put code in box, hit enter, when in lobby CTRL + Y, before joining new lobby ALT + Y to reload script and start with ALT + Y again.

!y:: ; Alt + Y to start the script.

InputBox, search, search, Enter search-term please.
MouseClick, left, 700, 400 ; Set for 2560x1440, use AutoHotkey Window Spy "Window" to find your coordinates
Sleep, 69 ; sleep after clicking on the input field
Send, %search%

Loop, ; Put the LFM Lobby number in the search field, then start the script. pause the script when lobby is joined.
{
MouseClick, left, 700, 400 ; Set for 2560x1440, use AutoHotkey Window Spy "Window" to find your coordinates
Sleep, 69 ; sleep after clicking on the input field
Send, {Enter} ; send enter to search
Sleep, 1150 ; sleep 1.15s to find the lobbies, might be different for you.

MouseClick, left, 1000, 500 ; Set for 2560x1440, use AutoHotkey Window Spy "Window" to find your coordinates

MouseClick, left, 1900, 250 ; Set for 2560x1440, use AutoHotkey Window Spy "Window" to find your coordinates
}


return