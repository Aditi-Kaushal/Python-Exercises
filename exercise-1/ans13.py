'''Question 13: - If five-digit number is input through the keyboard, write a program to reverse the
number.
'''
num=int(input("enter the five-digit number")) #12345
temp=num
rem1=temp%10 #5
temp=temp//10 #1234
rem2=temp%10 #4
temp=temp//10 #123
rem3=temp%10 #3
temp=temp//10 #12
rem4=temp%10 #2
temp=temp//10 #1
rem5=temp%10 #1
print("the reverse oder f the number is:",rem1,rem2,rem3,rem4,rem5)
