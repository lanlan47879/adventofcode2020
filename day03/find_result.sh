#!/bin/bash

total=1

tmp=`python3 day03_part02.py input.txt 1 1`

total=$(($total * $tmp))

tmp=`python3 day03_part02.py input.txt 1 3`

total=$(($total * $tmp))

tmp=`python3 day03_part02.py input.txt 1 5`

total=$(($total * $tmp))

tmp=`python3 day03_part02.py input.txt 1 7`

total=$(($total * $tmp))

tmp=`python3 day03_part02.py input.txt 2 1`

total=$(($total * $tmp))

echo $total
