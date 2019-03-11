#shell script to find the largest of two numbers
echo "Enter Num1"
read a;

echo "Enter Num2"
read b;

if [ $a = $b ]
then
  echo "both are equal";
elif [  $a -gt $b ]
then
  echo "$a is greater";
else
  echo "$b is greater";
fi
