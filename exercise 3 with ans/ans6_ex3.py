#Question 6: - If the three sides of a triangle are entered through the keyboard, write a program to
#check whether the triangle is isosceles, equilateral, scalene or right angled triangle
s1= int (input ("Enter the First side:"))
s2=int (input ("Enter the Second side:"))
s3=int (input ("Enter the Third side:"))
#for isosceles 2 sides must be equal
#for equilateral three side must be equal
#for for scalene all sides are different
#for right angled sum of squares of  2 sides equal to square of 3rd side
if s1 * s1 + s2 * s2 == s3 * s3:
    print("This is a Right Angled Triangle")
else:
    if s1 * s1 +s3 * s3 == s2*s2:
        print("This is a Right Angled Triangle")
    else:
        if s2 * s2 + s3 * s3 == s1*s1:
            print("This is a Right Angled Triangle")
        else:
           if s1 == s2 :
               if s1 != s3 :
                  print("This is an Isosceles Triangle")
               else:
                  print("This is an Equilateral Triangle")
           else:
               if s1 != s3:
                   if s2 != s3:
                       print("This is a Scalene Triangle")
                   else:
                        print("This is an Isosceles Triangle")
               else:
                     print("This is Isosceles Triangle") 
                
    
