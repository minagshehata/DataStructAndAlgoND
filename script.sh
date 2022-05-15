#!/bin/bash
FILE_NAME='./mina1.txt'
n=1
while read line;do 
	echo "Line no $n : $line"
	sed -i "s/$line//" "./mina.txt"
	n=$((n+1))
done < $FILE_NAME
