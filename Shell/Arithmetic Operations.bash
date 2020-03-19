read x
printf "%.03f" $(echo "scale=4; $x ;round=3"  | bc -l)
