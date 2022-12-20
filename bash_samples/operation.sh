#!/bin/bash

read X

if [ $X -lt -100  -o $X -gt 100 ]; then
    exit 1
fi

read Y

if [ $Y -lt -100 -o $Y -gt 100 -o $Y == 0 ]; then
    exit 1
fi

a=`echo " $X + $Y " | bc`
b=`echo " $X - $Y " | bc`
c=`echo " $X / $Y " | bc`
d=`echo " $X * $Y " | bc`
printf "$a\n$b\n$c\n$d"