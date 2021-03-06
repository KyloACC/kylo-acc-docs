$track = Read-Host -Prompt 'Input track name here'
$fuel = Read-Host -Prompt 'Input fuel per lap here'
$time = Read-Host -Prompt 'Input lap time in seconds here'

[decimal] $fuel_per_minute = [math]::round($fuel / $time * 60,3)
$minute = [math]::floor($time/60)
$second = $time - $minute * 60 
$fuel1 = [math]::Floor($fuel_per_minute * 25) + 6 
$fuel2 = [math]::Floor($fuel_per_minute * 45) + 6
$fuel3 = [math]::Floor($fuel_per_minute * 60) + 6

"| $track | $fuel | $fuel_per_minute | $minute : $second | $fuel1 | $fuel2 | $fuel3 |"
