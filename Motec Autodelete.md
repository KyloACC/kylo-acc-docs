# How to automatically delete motec that is 21d or older on logon

**Step 1: Create a ps1 file, name it whatever you want and enter the following:**
```bash
Get-ChildItem "$env:USERPROFILE\Documents\Assetto Corsa Competizione\MoTeC" -Recurse -File | Where CreationTime -lt  (Get-Date).AddDays(-21)  | Remove-Item -Force
```
$env:USERPROFILE should lead to your user profile.  

**Step 2: Go to Task Scheduler**  
![Task Scheduler](https://cdn.discordapp.com/attachments/498546852036083734/1086766897313362121/image.png "Task Scheduler")

**Step 3: Create a new Task with Logon as Trigger**  
![Trigger](https://cdn.discordapp.com/attachments/498546852036083734/1086766897716002826/image.png "Trigger")

**Step 4: Add running Powershell with a script as action**  
`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`  
`-file "C:\Users\lucaz\Documents\Delete motec data.ps1"`  
Has to be the location of your script.  

Now when you log-on it should delete all files older than 21 days in your selected directory. Hopefully if you did it right, you selected your Motec Directory.
