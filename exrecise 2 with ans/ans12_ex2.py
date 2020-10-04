'''Question 12: - Write a program to check whether a triangle is valid or not. When the three angles of
triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is
equal to 180 degrees.'''

angle_1= float (input ("Enter the First Angle of the Triangle:"))
angle_2= float (input ("Enter the Second Angle of the Triangle:"))
angle_3= float (input ("Enter the Third Angle of the Triangle:"))

result = angle_1 +angle_2 + angle_3
if result == 180:
    print("This is a Valid Triangle with sum =",result)
else:
    print("This is an invalid Triangle!!")
    
