num=int(input("enter the five-digit number"))

temp=num #let num=12345

rem=temp%10  #ans 5
sum=rem #sum=5
temp=temp//10 #1234
rem=temp%10 # 4
sum=sum+rem #4+5
temp=temp//10 #123
rem=temp%10 #3
sum=sum+rem #4+5+3
temp=temp//10 #12
rem=temp%10 #2
sum=sum+rem #4+5+3+2
temp=temp//10 #1
rem=temp%10 #1
sum=sum+rem #4 +5 +3 +2+ 1
print("sum of digits of number is:",sum)

