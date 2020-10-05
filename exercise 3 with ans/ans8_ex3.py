##Question 8: - A university has the following rules for a student to qualify for a degree with A as the
##main subject and B as the subsidiary subject:
##
##conditon-1 (a) He should get 55 percent or more in A and 45 percent or more in B.
##
##condition-2 (b) If he gets #less than 55 percent in A he should get 55 percent or more in B. However, he
##should get at least 45 percent in A.
##
##condition-3 (c) If he gets less than 45 percent in B and 65 percent or more in A he is allowed to reappear
##in an examination in B to qualify.
##
##condition -4 (d) In all other cases he is declared to have failed.
##
##Write a program to receive marks in A and B and Output whether the student has passed, failed or is
##allowed to reappear in B.

percentageA = float ( input ("Enter the percentage in A:"))
percentageB = float ( input ("Enter the percentage in B:"))

if percentageA >= 55:
    if percentageB >= 45:
        print("Candidate is  Passed")
    else:
        if percentageA >= 65:
            print("Candidate is allowed to RE-APPEAR in B")
        else:
            print("Candidate is marked FAIL")
else:
    if percentageB >= 55:
        print("Candidate must get 45% in A")
    else:
        print("Candidate is marked Fail")
        
