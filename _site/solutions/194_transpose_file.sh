
# # Given a text file file.txt, transpose its content.

# You may assume that each row has the same number of columns and each field is separated by the ' ' character.

# Example:

# If file.txt has the following content:

# name age
# alice 21
# ryan 30
# Output the following:

# name alice ryan
# age 21 30

while read line 
do 
	echo $line 
done < file.txt

awk '
{ 
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {    
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' file.txt