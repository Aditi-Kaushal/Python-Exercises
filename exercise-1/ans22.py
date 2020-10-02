'''Question 22: - Write a program that accepts an employee’s ID, total worked hours of a month and
the amount he received per hour. Print the employee’s ID and salary of a particular month.'''

employeeID=int(input("Enter the Employees' ID :"))

workinghrs=float(input("Enter the Total Worked Hours Of a Month :")) #5hrs per day 

amountPerHour=float(input("Enter the Amount Of per Hour :")) # he is getting 50 /- per hr 


print("Employees' ID is: ",employeeID)
print("Salary of a Particular Month is:",(workinghrs*30)*amountPerHour)
      
