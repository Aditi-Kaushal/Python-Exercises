num = int (input ("Enter Any Number:-"))

temp = num  #1265
if temp < 0:
    temp = temp * -1

sum = 0

while temp > 0:
    rem = temp % 10  #5 ,, 6,,2,,1
    sum = sum + rem
    temp = temp // 10

print( "Sum of Digit of Given Number:",sum)
