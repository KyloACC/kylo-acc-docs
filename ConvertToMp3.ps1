[string]$inputfile = Read-Host -Prompt 'Input file?'
[string]$outputfile = Read-Host -Prompt 'Output file?'
ffmpeg -i $inputfile -vn -ab 256 $outputfile