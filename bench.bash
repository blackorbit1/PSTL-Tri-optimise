#!/bin/bash

mkdir res
mkdir tab
make
python array_generator.py >/dev/null
for i in tab/*
do
  echo bench of $i
	./sort --file_in=$i --file_out=res/${i:4} 2>/dev/null
done

rm paths