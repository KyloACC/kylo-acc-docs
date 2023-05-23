#!/bin/bash

python3 'acc results companion csv modify'.py $1.csv
python3 add_stint.py output_file.txt $1.csv
python3 violins.py $1 $1 20
python3 boxplot.py $1 $1 $2 20 5
python3 linechart.py $1 $1 20