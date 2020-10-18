N=6 
  
# First Number of the 
# Fibonacci Series 
a=0 
  
# Second Number of the 
# Fibonacci Series 
b=1  
   
echo "The Fibonacci series is : "
   
for (( i=0; i<N; i++ )) 
do
    echo -n "$a "
    fn=$((a + b)) 
    a=$b 
    b=$fn 
done#!/bin/bash
printf "Ievadiet skaitli: "; read a

re='^[0-9]+$'
until [[ $a =~ $re ]]
do
  printf "Error: Ievadītā vērtība nav skaitlis! Ievadiet skaitli: "; read a
done
