#!/bin/bash

i=1

until [ $i -gt 25 ]
do
    if [ ! -d "Day$i" ]; then
        mkdir Day$i
    fi
    touch Day$i/code_day_$i.py
    cat .base.py > Day$i/code_day_$i.py
    ((i=i+1))
done