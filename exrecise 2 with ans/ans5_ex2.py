n1 = int (input ("Enter First Number:"))
n2 = int (input ("Enter the Second Number:"))
n3 = int ( input ("Enter the Third Number:"))

if n1 == n2 :
    if n1 == n3:
        print("All the Three Numbers are Equal")
    else:
        if n1 > n3 :
            print("First and Second Numbers are Largest")
        else:
            print("Third Number is Largest")
else:
    if n1 == n3:
        if n1 > n2 :
            print("First and Third Number are Largest")
        else:
            print("Second Number is Largest")
    else:
        if n2 == n3:
            if n2 > n1:
                print("Second and Third Number are Lagest")
            else:
                print("First Number is Largest")
        else:
            if n1 > n2 :
                if n1 > n3 :
                    print("Firs Number is Largest")
                else:
                    print("Third Number is Largest")
            else:
                if n2 > n3 :
                    print("Second Number is Largest ")
                else:
                    print("Third Number is Largest")
                    
        
