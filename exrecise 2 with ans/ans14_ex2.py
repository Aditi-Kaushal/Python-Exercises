#Question 14: - Input length and breadth of a rectangle, write a program find whether the area of the
#rectangle is greater than its perimeter.
length= float (input ("Enter the Length of Rectangle:"))
breadth= float (input ("Enter the Breadth of Rectangle:"))
area = length * breadth
paremeter = 2 * ( length + breadth )
if area > paremeter:
    print("YES, Area is Greater than Paremeter:","area:",area,"paremeter:",paremeter)
else:
    print("NO, Area is less than parameter:","area:",area,"paremeter:",paremeter)
