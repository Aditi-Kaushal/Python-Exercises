'''Question 18: - Write a program to accept a coordinate point in XY coordinate system and determine
in which quadrant the coordinate point lies.
'''
x = int( input ("Enter the value of  x:"))
y = int( input("Enter the  value of y:"))
print((x,y))

if x > 0 :
    if y > 0 :
        print("The Point Lies in the 1ST Quadrant")
    else:
        print("The Point Lies in the 4TH Quadrant")
else:
    if x <0:
        if y > 0:
            print("The Point Lies in the 2ND Quadrant")
        else:
            print("The Point Lies in the  3RD Quadrant",(x,y))
        
