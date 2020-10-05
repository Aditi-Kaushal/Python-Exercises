'''Question 5: - If the three sides of a triangle are entered through the keyboard, write a program to
check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than
the largest of the three sides.
'''
s1=int (input ("Enter the First side of the Triangle:"))
s2=int (input ("Enter the Second side of the Triangle:"))
s3=int (input ("Enter the Third side of the Triangle:"))

if s1 + s2 == s3:
    print("sum of 1st and 2nd side is equals to 3rd side,This is a Valid Triangle:",s1+s2)
elif s1 + s3 == s2:
    print("sum of 1st and 3rd side is equals to 2nd side,This is a Valid Triangle:",s1+s3)
elif s2 + s3 == s1:
    print("sum of  2nd and 3rd  side is equals to 1st side,This is a Valid Triangle:",s2+s3)
else:
    print("Triangle is not valid")
        
