$fuel = Read-Host -Prompt 'Input fuel per lap here'
[string]$time = Read-Host -Prompt 'Input lap time here'
[int]$maxtime = Read-Host -Prompt 'Input race length here'


[int]$temp = ($time.Length-2)
[int]$minute = $time.Substring(0,1)
[decimal]$second = $time.Substring(2,$temp)


$time2 = ($minute * 60 + $second)

[decimal] $fuel_per_minute = [math]::round($fuel / $time2 * 60,3)

$laps = [math]::ceiling( (($maxtime*60) / $time2))
$result = [math]::round([math]::ceiling($fuel_per_minute * $maxtime) + $fuel)

"$result"
""
""
"$result litres of fuel for $laps laps and one extra lap. [Laptime: $minute minute(s) and $second seconds] & [Race length: $maxtime minutes] & [$fuel litres per lap]"
