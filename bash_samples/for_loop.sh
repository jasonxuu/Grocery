#!/bin/bash

#Your task is to use for loops to display only odd natural numbers from  1 to 99.

for (( i=0; i<100; i++));
do
  x=$(($i % 2))
  if [ $x == 1 ]
  then
      printf "$i\n"
  fi
done