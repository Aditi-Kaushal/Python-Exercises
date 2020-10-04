'''Question 20: - Write a program to read temperature in centigrade and display a suitable message
according to temperature state below:
temperature < 0 then freezing weather
temperature between 0 and 10 then Very Cold Weather
temperature between 10 and 20 then Cold Weather
temperature between 20 and 30 then Normal Weather
temperature between 30 and 40 then Its hot Weather
temperature >= 40 then Its very hot weather'''

t= float(input ("Enter the Temperature in Centigrade:"))
if t < 0:
    print("Freezing Weather")
else:
    if t <= 10:
        print("Very Cold Weather")
    else:
        if t <= 20:
            print("Cold Weather")
        else:
            if t <= 30:
                print("Normal Weather")
            else:
                if t <=40:
                    print("Its Hot Weather ")
                else:
                    if t >=40:
                        print("Its Very Hot Weather")
                    else:
                        print("Enter the Suitable Temperature!!")
    
        
        
