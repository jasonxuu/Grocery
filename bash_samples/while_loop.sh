#!/bin/bash

read num

total=$num
sum_num=0

if [ $num -lt 1 -o $num -gt 500 ]; then
    echo "The range of numbers is from 1 to 500"
    exit 1
fi

while true
do
  if [ $total == 0 ]; then
      echo "scale=3; $sum_num / $num" | bc
      exit 0
  else
    read inter
    if [ $inter -lt -10000 -o $inter -gt 10000 ]; then
        echo "The input of number is out of range[-10000, 10000]"
        exit 1
    else
      total=$((total - 1))
      sum_num=$((sum_num + inter))
    fi

  fi

done