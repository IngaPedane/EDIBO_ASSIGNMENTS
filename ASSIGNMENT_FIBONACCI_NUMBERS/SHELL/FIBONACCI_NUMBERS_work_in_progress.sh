#!/bin/bash

printf "Ievadiet skaitli: "; read N

re='^[0-9]+$'
until [[ $N =~ $re ]]
do
  printf "Error: Ievadītā vērtība nav skaitlis! Ievadiet skaitli: "; read N
done
#a=0 
#b=1  
   
echo "Pirmie $N Fibonači skaitļi ir:"
#   
#for (( i=0; i<N; i++ )) 
#do
#    echo -n "$a "
#    fn=$((a + b)) 
#    a=$b 
#    b=$fn 
#done
x=0
y=1
i=2
#  echo ""
  echo "$x"
  echo "$y"
while [ $i -lt $N ]
do
      i=`expr $i + 1 `
      z=`expr $x + $y `
      echo "$z"
      x=$y
      y=$z
done

