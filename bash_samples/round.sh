#!/bin/bash

read expression

b=`echo "scale=5; $expression " | bc`

printf "%.3f" "$b"
#echo "$b" | xargs printf "%.*f\n" "3"