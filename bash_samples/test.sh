#!/bin/bash

while true
do
  read line
  num=${#line}
  if [ $num -gt 100 -o $num -lt 1 ]; then
      printf "lenght of input is limited: [1,100], retry"
      exit 1
  else
      echo "$line" | cut -b 3
  fi

done