# How to automatically delete motec that is 21d or older on logon

Step 1: Create a ps1 file, name it whatever you want and enter the following:
```bash
Get-ChildItem "C:\Users\lucaz\Documents\Assetto Corsa Competizione\MoTeC" -Recurse -File | Where CreationTime -lt  (Get-Date).AddDays(-21)  | Remove-Item -Force
```

You will obviously have to change `lucaz` to your own Windows username.


Step 2: Go to Task Scheduler  
![Task Scheduler](https://i.vgy.me/SdEVla.png "Task Scheduler")

Step 3: Create a new Task with Logon as Trigger  
![Trigger](https://i.vgy.me/mdziup.png "Trigger")

Step 4: Add running Powershell with a script as action  
`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`  
`-file "C:\Users\lucaz\Documents\Delete motec data.ps1"`  
Has to be the location of your script.  
![Trigger](https://i.vgy.me/mdziup.png "Trigger")

Now when you log-on it should delete all files older than 21 days in your selected directory. Hopefully if you did it right, you selected your Motec Directory.