"""Question 17: - Input a point (x,y), write a program to find out if it lies on the x-axis, y-axis or at the
origin"""
x= int (input ("Enter the value of x:"))
y= int (input ("Enter the value of y:"))
print((x,y))
if x==0:
    if y != 0:
        print("The Point Lies on y-axis")
    else:
        print("The Point Lies on the Origin")
else:
    if y ==0 :
        if x != 0:
            print("The Point Lies on x-axis")
        else:
            print("The Point Lies on y-axis")
            
        
