'''Question 3: - A certain grade of steel is graded according to the following conditions:
i) Hardness must be greater than 50
ii) Carbon content must be less than 0.7
iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Write a program, which will require the user to give values of hardness, carbon content and tensile
strength of the steel under consideration and output the grade of the steel.
'''
hardness= int (input ("Enter the Hardness of the Steel:"))

carbon= float (input ("Enter the Carbon Content of the Steel:"))

tensile= int (input ("Enter the Tensile Strength of the Steel:"))

if hardness  > 50:
    if carbon < 0.7:
        if tensile > 5600:
            print("Grade is : 10") # three condition met
        else:
            print("Grade is :9") # two condition met
    else:
        if tensile > 5600:
            print("Grade is : 7") # 1 ans 3 true
        else:
            print("Grade is : 6") # only 1 true
else:
    if carbon < 0.7:
        if tensile > 5600:
            print("Grade is : 8") #only 2nd ans 3rd  true
        else:
            print("Grade is :6") #only 2nd true
    else:
         if tensile > 5600:
             print("Grade is : 6") #only 3 true
         else:
             print("Grade is : 5") #no one is true
        
