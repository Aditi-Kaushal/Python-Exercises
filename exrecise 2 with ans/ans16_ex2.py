'''Question 16: - Input the coordinates (x,y) of a center of a circle and its radius. Input another point
(x1,y1). Write a program to check given point lies inside the Circle, on the Circle or outside the Circle.
'''
x = int ( input ("Enter the Co-ordinate of x:"))
y = int ( input ("Enter the co-ordinate of y:"))
print("The Center of a Circle is :",(x,y))
r = int ( input ("Enter the Radius of Circle:"))
x1 = int ( input ("Enter the value of x1:"))
y1 = int ( input ("Enter the value of y1:"))
result =(x1-x)*(x1-x)  + (y1-y)*(y1-y)
if result <= (r*r) :
    print("Point is Inside the Circle:",result)
elif (x1*x1) + (y1*y1) == r*r :
    print("The Point Lies on the Circle")
else:
    print("Point is Outside the Circle")
