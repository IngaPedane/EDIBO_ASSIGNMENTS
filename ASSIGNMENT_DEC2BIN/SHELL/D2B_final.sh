#!/bin/bash
printf "Ievadiet skaitli: "; read a

re='^[0-9]+$'
until [[ $a =~ $re ]]
do
  printf "Error: Ievadītā vērtība nav skaitlis! Ievadiet skaitli: "; read a
done
b=$a

array=()

while [ $a != 0 ]
do
array+=$(($a%2))
a=$(($a/2))
done 

c=$(echo "${array[*]}" | rev)
echo "Binārā vērtība skaitlim $b ir:" $c


