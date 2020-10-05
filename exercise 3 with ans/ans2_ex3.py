'''Question 2: - An insurance company follow following rules to calculate premium.
i) If a person’s health is excellent and the person is between 25 and 35 years of age and
lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount
cannot be exceeded Rs. 2 Lakhs.
ii) If a person satisfies all the above conditions except that the gender is female then the
premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 Lakh.
iii) If a person’s health is poor and the person is between 25 and 35 years of age and lives in
a village and is a male then the premium is Rs. 6 per thousand and his policy amount
cannot exceed Rs. 10000.
iv) In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and
maximum amount for which he/she can be insured.
'''
health= str(input ("Enter the Health of the Candidate:"))
age = int (input ("Enter the Age of the Candidate:"))
residance = str (input ("Enter the village or city of Candidate:"))
gender = str (input ("Enter the Gender of the Candidate:"))
if health == "excellent":
    if age > 25:
        if age < 35:
            if residance == "city":
               if gender == "male" :
                   premium = "RS 4 per thousand"
                   policy = "less than 2 lakh"
                   print("The Premium Rate  of the Candidate is :",premium)
                   print ("The Policy Amount should be :",policy)
               else:
                    premium = "RS 3 per thousand"
                    policy = "less than 1 lakh"
                    print("The Premium Rate  of the Candidate is :",premium)
                    print ("The Policy Amount should be :",policy)
            else:
                print ("Recheck the Information You have entered")
        else:
            print("Your Age is above 35 so, you can't get insured!!!")
    else:
        print("Your Age is lesser than 25 so, you can't get insured!!!")
else:
    if health == "poor":
        if age > 25:
            if age < 35:
                if residance == "village":
                    if gender == "male" :
                        premium = "RS 6 per thousand"
                        policy = "less than 10000 lakh"
                        print("The Premium Rate  of the Candidate is :",premium)
                        print ("The Policy Amount should be :",policy)
                    else:
                       print("Recheck the Information You have entered")
                else:
                  print("you can't get insured!!!")
            else:
               print ("Your Age is above 35 so, you can't get insured!!!")
        else:
            print("Your Age is above 25 so, you can't get insured!!!")
    else:
        print("You haven't entered suitable health ")

                    
             
                    
