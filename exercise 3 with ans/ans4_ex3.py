'''Question 4: - A library charges a fine per every book, returned late. For first 5 days the fine is 50
paise, for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after
30 days your membership will be cancelled. Write a program to accept the number of days the
member is late to return the book and display the fine of the appropriate message.
'''

days = int (input ("Enter the Number of Days of being late to submit the book:"))
if days > 0 :
    if days <= 5:
        fine = "50 paise"
        print("You are  late to submit the book soo, You have to pay Fine is :",fine)
    else:
        if days >= 6:
            if days <= 10:
                fine = "1 rupees"
                print ("You are  late to submit the book soo, You have to pay Fine is :",fine)
            else:
                if days <= 29:
                    fine = "5 rupees"
                    print("You are late for above 10 Days to submit the book soo, You have to pay Fine is :",fine)
                else:
                    if days >= 30:
                        print("you return the book after 30 days your membership has been cancelled!!")
                    else:
                        print("Enter the correct input")
        else:
            print(" Enter the correct input ")
else:
    print("Enter the correct input ")
             
            
                
                    
       
                    
                




    
