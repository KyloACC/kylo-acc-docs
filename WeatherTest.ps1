[string]$track = Read-Host -Prompt 'Input track here'
[string]$championship = Read-Host -Prompt 'Input championship here'
[int]$number = Read-Host -Prompt 'Input number of images here'


magick montage -background none -tile 1x$number -geometry +0+0 AC2* WeatherTest-$championship-$track.png