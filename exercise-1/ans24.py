'''Question 24: - Write a program to read an amount and break the amount into smallest possible
number of bank notes.'''
amount=int ( input ("Enter the Amount:"))

temp=amount 

notes=temp//2000 
print("Number of 2000 Note:",notes)
temp=temp%2000 

notes = temp//500 
print("Number of 500 Note:",notes)
temp=temp%500

notes= temp//200
print("Number of 200 Note:",notes )
temp=temp%200

notes = temp//100
print("Number of 100 Note:",notes)
temp=temp%100

notes =temp//50
print("Number of 50 Notes:",notes )
temp=temp%50

notes = temp//20
print("Number of 20 Notes:",notes)
temp=temp%20

notes = temp//10
print("Number of 10 Notes:",notes)
temp=temp%10

notes =temp//5
print("Number of 5 Notes:",notes )
tep=temp%5

notes = temp//2
print("Number of 2 Notes:",notes )
temp=temp%2
notes=temp
print("Nmber of 1 Notes:",notes)
