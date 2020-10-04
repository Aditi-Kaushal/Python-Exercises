"""Question 8: - Input two number and check first number is divisible by second number"""
n1 = int (input ("Enter the first Number :"))
n2 = int (input ("Enter the Second Number:"))
result=n1/n2
if n1 % n2 == 0:
    print(result)
    print("YES,First Number is Divisible by Second Number")
else:
    print("NO,First Number is not Diivisible by Second Number")
