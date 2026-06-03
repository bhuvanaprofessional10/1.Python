class SubfieldsInAI():
    def sub_fields():
        AIList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print(" Sub-fields in AI are:")
        for sub in AIList:
            print("\n",sub)


class OddEven():
    # Create a  function to check the given number is even or odd
    def check_odd_even(number):    
        #check the input is odd or even    
        if((number%2)==0):
            print("Your input is even number")
            message="even"
        else:
            print("Your input is odd number")
            message="odd"
        return message

class ElegiblityForMarriage():
    # Create a  function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def marriage_eligibility_check(age,gender):
        if(gender == "female"):
            if(age  <18):
                diff=18-age
                print(f"You are not eligible for marriage yet. You have to wait {diff} more years to get into marriage life !")
                eligibleInd="You are NOT eligible for marriage yet. "
            else:
                print("Your are eligible for marriage.")
                eligibleInd="Congrats... You are eligible for Marriage"
        else:
            if(age  <21):
                diff=21-age
                print(f"You are not eligible for marriage yet. You have to wait {diff} more years to get into marriage life !")
                eligibleInd="You are NOT eligible for marriage yet. "
            else:
                print("Your are eligible for marriage.")
                eligibleInd="Congrats... You are eligible for Marriage"
        return eligibleInd    

class FindPercent():

    @staticmethod
    def percentage(mark_list):    
        total_mark=0
        for mark in mark_list.values():
            total_mark=total_mark+mark
        #print(f"Mark total: {total_mark}")
        percentage = total_mark / len(mark_list)
        return total_mark,percentage
    
    def get_percentage():
        name=input("enter your name")
        rollnumber=input("enter your roll number")
        #mark_list=[85,80,99,97,92]
        mark_list = {"Tamil":90,"English":85,"Math":100,"Science":98,"Social":92}
        total, percent = FindPercent.percentage(mark_list)
        if(percent >35):
            status="Pass"
        else:
            status="Fail"
            
        print(f"Congratulation .....  {name} !!!!!!. Please find your details as below")
        print("--------------------")
        print(f"Roll number : {rollnumber}")
        print(f"Name        : {name}")
        for sub,mark in mark_list.items():
            print(f"{sub}       : {mark}")    
        print(f"Mark total  : {total}")
        print(f"Percentage  : {percent}")
        print(f"Status      : {status}")
        print("--------------------")


class Triangle():
    def calc_triangle_area():
        height=float(input("enter the height of triangle"))
        width=float(input("enter the width of triangle"))
        area=(height*width)/2
        print("height :",height)
        print("width :",width)
        print("Area formula : (height*width)/2")
        print("Area of Triangle: :",area)        
        return area

    def calc_triangle_peri():
        height1=float(input("enter the height1 of triangle"))
        height2=float(input("enter the height2 of triangle"))
        width=float(input("enter the width of triangle"))
        peri=height1+height2+width
        print("height1 :",height1)
        print("height2 :",height2)
        print("width :",width)
        print("perimeter formula : (height1 + height2 + width)")
        print("perimeter of Triangle: :",peri)
        return peri