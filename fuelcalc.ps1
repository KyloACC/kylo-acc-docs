$fuel = Read-Host -Prompt 'Input fuel per lap here'
[string]$time = Read-Host -Prompt 'Input lap time here'
$maxtime = Read-Host -Prompt 'Input race length here'

[int]$minute = $time.Substring(0,1)
[int]$second = $time.Substring(2,2)

$time2 = ($minute * 60 + $second)

[decimal] $fuel_per_minute = [math]::round($fuel / $time2 * 60,3)

$result = [math]::round($fuel_per_minute * $maxtime + $fuel + $fuel)

" $result "
