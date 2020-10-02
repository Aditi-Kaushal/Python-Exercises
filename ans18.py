'''Question 18: - If a five-digit number is input through the keyboard, write a program to print a new
number by adding one to each of its digits. For example, if the number that is input is 12391, then,
the output should be displayed as 23402.'''
num=int(input("enter the five digit number:")) # 12391
temp = num

rem=temp%10 #1
result=(rem +1)%10 #2%10=2
temp=temp//10 #1239
rem=temp%10 #9
result=((rem +1)%10)*10 +result #2
temp=temp//10#123
rem=temp%10 #3
result=((rem +1)%10)*100+result #402
temp=temp//10#12
rem=temp%10 #2
result=((rem +1)%10)*1000+result #3000+402=3402
temp=temp//10 #1
rem=temp%10  #1
result=((rem +1)%10)*10000+result #20,000+3402=23402
print("NEW NUMBER IS:",result)
 

