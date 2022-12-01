#!/bin/bash

mkdir Day{2..24}
touch Day{2..24}/input.txt
touch Day{2..24}/example.txt

for i in {2..24..1}
do
    cp code.py Day$i/
done

mv code.py code2.py

for i in {2..24..1}
do
    cp code2.py Day$i/
done
