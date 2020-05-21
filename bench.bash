#!/bin/bash

cmake -DCMAKE_BUILD_TYPE=Release
make

mkdir -p res
mkdir -p tab

for i in tab/*
do
  echo bench of $i
  ./sort --file_in=$i --file_out=res/${i:4} 2>/dev/null
done
