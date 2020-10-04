'''Question 19: - Write a program to calculate the root of a quadratic equation.
'''
from math import*
print("Quadratic Equation is : ax^2+bx+c")
a= int( input("Enter value of a:")) #ax^2-bx+c
b= int( input("Enter value of b:"))
c= int( input("Enter value of c:"))

d= (b*b - 4 * a* c)
d = sqrt ( abs(d) )
if d > 0:
    x1= (-b + d) / (2 * a)
    x2= (-b - d) / (2 * a)
    print("Roots of the Given Quadratic Equation:","{",x1,":",x2,"}")
else:
    print("Enter the Valid Quadratic Eqution")
