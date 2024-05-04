#!/bin/bash

read EXPRESSION
ANSWER=$(echo "scale=10; $EXPRESSION" | bc)
ROUNDED=$(printf "%.3f" $ANSWER)
echo $ROUNDED
