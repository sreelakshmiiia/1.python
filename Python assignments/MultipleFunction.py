class MultiFunctions():
    def Subfields():
        subfieldlist=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for temp in subfieldlist:
            print(temp)
    # Odd or even        
    def oddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")
     # Marriage eigibility check       
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender.lower()=="male"):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender.lower()=="female"):
            if(age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("not applicable")
     # Calculate Percentage       
    def percentage():
        num=int(input("Count of subjects:"))
        total=0
        for i in range(num):
            marks=int(input(f"Subject{i+1}:"))
            total=total+marks
        print("Total=",total)
        percentage=total/(num*100)*100
        print("Percentage:", percentage)      
     #Triangle functions   
    def area():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=h*b/2
        print("Area of triangle=", area)
    def perimeter():
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=h1+h2+b
        print("Perimeter of triangle",perimeter)    