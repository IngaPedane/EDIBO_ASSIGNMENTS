#!/bin/bash

echo Dotais skaitlis: $1
c=$1;
b=$c;

#a=0; b=0; #b0=0; b1=0; b2=0; b3=0; b4=0; b5=0; b6=0; b7=0;

#a=$(($c/2)); b=$(($c%2)); b0=$b
#echo $a $b $b0
#a=$(($a/2)); b=$(($a%2)); b1=$b
#echo $a $b $b1
#a=$(($a/2)); b=$(($a%2)); b2=$b
#echo $a $b $b2

echo "c mainīgā vērtība pirms cikla: " $c
echo ' '

while [ $c != 0 ]
do
  c=$(($c/2))
  echo "c mainīgā vērtība ciklā: " $c
  echo "atlikums no dalījuma c:  " $(($c%2))
  echo ' '
done

echo "c mainīgā vērtība pēc cikla: " $c
echo ' '

######### Kā izprintēt loop mainīgos vienā rindā? #########
echo Binārā vērtība skaitlim $1:

until [ $b != 0 ]
do
  echo $b%2
  b=$(($b%2))
  echo ' '
done

while [ $b != 0 ]
do
  b=$(($b/2))
  echo $(($b%2))
done

