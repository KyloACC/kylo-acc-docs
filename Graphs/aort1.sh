#!/bin/bash

rm output*.txt

files=("boothby" "alexander" "allan" "alvarado" "barrier" "dimitrov" "foch" "geert" "gold_saw" "greko" "honzik" "melis" "riba" "richie" "schubert" "whitehead")

for file in "${files[@]}"
do
	echo "$file"
	python3 aor_t1.py "$file"
	python3 average.py "$file" > "output2_T1_$file.txt"
done

python3 aor_all_t1.py "$1" $2
