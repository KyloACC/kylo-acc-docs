$fuel = Read-Host -Prompt 'Input fuel per lap here'
[string]$time = Read-Host -Prompt 'Input lap time here'
[int]$maxtime = Read-Host -Prompt 'Input race length here'

[int]$minute = $time.Substring(0,1)
[int]$second = $time.Substring(2,2)

$time2 = ($minute * 60 + $second)

[decimal] $fuel_per_minute = [math]::round($fuel / $time2 * 60,3)

$laps = [math]::ceiling( (($maxtime*60) / $time2))
$result = [math]::round([math]::ceiling($fuel_per_minute * $maxtime) + $fuel)

" $result litres of fuel for $laps laps and one extra lap."
