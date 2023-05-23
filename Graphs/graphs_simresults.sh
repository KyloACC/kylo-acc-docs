#!/bin/bash

python3 modify_laptimes.py $1.txt > output.csv
python3 add_stint.py output.csv $1.csv
echo "title for graph?"; read title
python3 violins.py $1 $1 5 "$title"
python3 boxplot.py $1 $1 "$title" 5 10
python3 linechart.py $1 $1 5 "$title"
python3 linechart_movingaverage.py $1 $1 5 "$title"