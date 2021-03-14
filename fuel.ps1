$Car = Read-Host -Prompt 'Input Car here'
$track = Read-Host -Prompt 'Input track name here'
$fuel = Read-Host -Prompt 'Input fuel per lap here'
$time = Read-Host -Prompt 'Input lap time in seconds here'


[int]$minute = $time.Substring(0,1)
[int]$second = $time.Substring(2,2)

$time2 = ($minute * 60 + $second)

[decimal] $fuel_per_minute = [math]::round($fuel / $time2 * 60,3)
$fuel1 = [math]::Floor($fuel_per_minute * 25) + 6 
$fuel2 = [math]::Floor($fuel_per_minute * 45) + 6
$fuel3 = [math]::Floor($fuel_per_minute * 60) + 6

"| $track 	| $fuel 		| $fuel_per_minute 		| $time 			| $fuel1 		| $fuel2		 | $fuel3 		|"

"$Car 
| $track 	| $fuel 		| $fuel_per_minute 		| $time 			| $fuel1 		| $fuel2		 | $fuel3 		|" | Out-File -FilePath 'C:\Users\lucaz\Documents\Assetto Corsa Competizione\Setups\fuel_calc.txt' -Append

