#!/bin/bash
#taking 3 integers
read X
read Y
read Z

#determining type of triangle
if [[ $X == $Y && $Y == $Z ]]
then
  echo EQUILATERAL
elif [[ $X == $Y || $X == $Z || $Y == $Z ]]
then
  echo ISOSCELES
else
  echo SCALENE
fi
