$ambient_a = Read-Host -Prompt 'Input ambient temperature of setup'
$ambient_b = Read-Host -Prompt 'Input ambient temperature'
$track_a = Read-Host -Prompt 'Input track temperature of setup'
$track_b = Read-Host -Prompt 'Input track temperature of setup'


$result1=$ambient_a-$ambient_b
$result2=$track_a-$track_b
"$result1"
"$result2"
$pressure_change = [math]::max(($ambient_a-$ambient_b)*0.1, ($track_a-$track_b)*0.05)
"$pressure_change"