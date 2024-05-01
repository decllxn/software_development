#!/bin/bash

#Taking user input
read CHARACTER

if [[ $CHARACTER =~ [yYnY] ]]
then
  if [[ $CHARACTER == Y || $CHARACTER == y]]
  then
    echo YES
  else
    echo NO
  fi
fi
