#Question 21: - Write a Program to check whether given number is multiple of 3 or 7
num = float(input ("Enter any Number:"))
if num % 3 == 0:
    if num % 7 == 0:
        print("YES, Number is Multiple of  3 and 7 :")
    else:
        print("Number is a Multiple of 3")
else:
    if num % 7 ==0:
        if num % 3==0:
            print("YES, Number is Multiple of  3 and 7 ")
        else:
            print("Number is a Multiple of 7")
    else:
        print(" Number is not a Multiple of 3 or 7 !!")
