#! /bin/bash

Echo Number given: $1
c=$1

x=$(($c/2)); y=$(($c%2)); ba=$y
x=$(($x/2)); y=$(($y%2)); ba=$y

echo "c mainīgā vērtība pirms cikla: " $c
while [ "$c" != 0 ]
do
  c=$(($c/2))
  echo "c mainīgā vērtība ciklā: " $c
done	
echo "c mainīgā vērtība pēc cikla: " $c
