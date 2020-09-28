print("Question 8: - If the marks obtained by a student in five different subjects are input through keyboard. Write a program to find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by a student in each subject is 150.")

print("MARKS OF A STUDENT IN FIVE DIFFERENT SUBJECTS:")
MATHS=float(input("enter the marks of MATHS:"))
ENGLISH=float(input("enter the marks ENGLISH:"))
HINDI=float(input("enter the marks HINDI:"))
SCIENCE=float(input("enter the marks SCIENCE:"))
SST=float(input("enter the marks SST:"))

aggregate=MATHS+ENGLISH+HINDI+SCIENCE+SST
print("AGGREGATE MARKS ARE:",aggregate)
percentage=(aggregate/500*100)
print("PERCENTAGE IS:",percentage)
