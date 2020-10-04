#Question 15: - Input three points (x1,y1), (x2,y2) and (x3,y3). Write a program to check if all the
#three points fall on the straight line or not.

x1 = int (input ("Enter the value of x1:"))
y1 = int (input ("Enter the value of y1:"))
x2 = int (input ("Enter the value of x2:"))
y2 = int (input ("Enter the value of y2:"))
x3 = int (input ("Enter the value of x3:"))
y3 = int (input ("Enter the value of y3:"))

if x1 > 0:
    if y1 > 0:
        if x2 > 0:
            if y2 >0:
                if x3 > 0:
                    if y3 > 0:
                        print("YES, ALL the Three Points Lies on the Straight Line")
                    else:
                        print("NO, These three Pointd Do Not Lies On The Straight Line")
                else:
                    print("NO, These three Pointd Do Not Lies On The Straight Line ")
            else:
                print("NO, These three Pointd Do Not Lies On The Straight Line")
        else:
            print("NO, These three Pointd Do Not Lies On The Straight Line ")
    else:
        print("NO, These three Pointd Do Not Lies On The Straight Line ")
else:
    print("NO, These three Pointd Do Not Lies On The Straight Line ")
    
    
    
        
