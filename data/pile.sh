#!/bin/bash
rm -rfv pile
mkdir pile
for input in $(find . -name "*.jsonl.bz2")
do
    echo Adding $input
    bzcat $input >> pile/pile.jsonl
done
echo Compressing the pile
bzip2 -v -9 pile/pile.jsonl
