##Question 7: - In a company, worker efficiency is determined on the basis of the time required for a
##worker to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the
##worker is said to be highly efficient. If the time required by the worker is between 3 – 4 hours, then
##the worker is ordered to improve speed. If the time taken is between 4 – 5 hours, the worker is given
##training to improve his speed, and if the time taken by the worker is more than 5 hours, then the
##worker has to leave the company. If the time taken by the worker is input through the keyboard,
##find the efficiency of the worker.
##
##condition-1:If the time taken by the worker is between 2 – 3 hours, then the
##worker is said to be highly efficient
##
##condition-2:If the time required by the worker is between 3 – 4 hours, then
##the worker is ordered to improve speed.
##
##condition-3:If the time taken is between 4 – 5 hours, the worker is given
##training to improve his speed
##
##condition-4:if the time taken by the worker is more than 5 hours, then the
##worker has to leave the company

time= int (input ("Enter the Time taken by the Worker :"))
print("-----------------------------------Efficiency of the woker--------------------------------------")
if time > 2 :
    if time < 3 :
        print("Worker is Highly Efficient:","As he/she is taking:",time,"hours")
    else:
        if time < 4:
            print("The Worker is ordered to improve Speed:","As he/she is taking:",time,"hours")
        else:
            if time < 5:
                print("Worker will be given training to improve his/her Speed:","As he/she is taking:",time,"hours")
            else:
                print("Worker has to Leave the Company:","As he/she is taking:",time,"hours")
else:
    print("enter the Valid time of the Worker!!!")

