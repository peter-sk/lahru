#!/bin/bash
output=$1
shift
for input in "$@"
do
    echo Adding $input
    bzcat $input >> $output.jsonl
done
echo Compressing $output.jsonl
bzip2 -vv -9 $output.jsonl
