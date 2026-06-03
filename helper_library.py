class helper():
    def subraction(n1,n2):
        sub=n1-n2
        return sub

    #function with parameter
    def addition(n1,n2):
        add=n1+n2
        return add

    #BMI check 
    def calculate_bMI():
        bmi=float(input("Enter your BMI"))
        if(bmi <18.5):
            print("You are Underweight")
            message="Underweight"
        elif(bmi < 24.9):
            print("You are Healthy . Your are in Normal Weight. Keep continue your current diet")
            message="Normal weight"
        elif(bmi < 29.9):
            print("You are Overweight. Need to take action on your diet")
            message="Overweight"
        elif(bmi < 34.9):
            print("You are Obesity Class 1. Need to do regular exercise along with diet ")
            message="Obesity Class 1"
        elif(bmi < 39.9):
            print("You are Obesity Class 2. Need to consult your doctor")
            message="Obesity Class 2"
        else:
            print("You are Extreme Obesity. Need a immediate doctor consultation ")
            message="Extreme Obesity"
        return message

    def check_odd_even():    
    #check the input is odd or even
        number = int(input("enter your input"))
        if((number%2)==0):
            print("Your input is even number")
            message="even"
        else:
            print("Your input is odd number")
            message="odd"
        return message

    #function for person classification based on age
    #age < 18 -> kid age < 35 -> adult age < 59 -> citizen age >59 -> senior citizen
    

    def age_category_bylist():
        agelists=[23,46,84,76,9]
        for age in agelists:
            if(age <18 ):
                print(age," - you are kid")
            elif(age <35):
                print(age, "- you are adult")
            elif(age <59):
                print(age,"- you are citizen")
            else:
                print(age,"- You are senior citizen")

    def age_category():
        age = int(input("enter your age"))
        if(age <18 ):
            print("you are kid")
            cate= "Children"
        elif(age <35):
            print("you are adult")
            cate= "Adult"
        elif(age <59):
            print("you are citizen")
            cate= "Citizen"
        else:
            print("You are senior citizen")
            cate= "Senior citizen"
        return cate