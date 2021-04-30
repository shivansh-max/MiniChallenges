_Auther_="shivansh"

# I love HARRY POTTER
#print("Hello World")


import math
import random
import turtle



def bang():

    thing=input("What would you like to do first, the Calculator or the game (please copy the same spelling).")

    if thing=="Calculator":
        print("This is a calculator and this will find a lot of cool things in math.")
        def rac():
            Operation=input("""What is the operation you would like to do(+,-,*,/,%, squared, area, perimeter,factors, square root)(please copy the same spelling)
""")
            if Operation=="+":
                N1=int(input("What is the first number is the first number you would like to use:"))
                N2=int(input("What is the second number"))
                print("SUM",N1+N2)
            if Operation=="-":
                N1=int(input("What is the first number is the first number you would like to use:"))
                N2=int(input("What is the second number"))
                if N1 < N2:
                    tab=N1
                    N1=N2
                    N2=tab
                print("DIFFRENCE",N1-N2)
            if Operation=="*":
                N1=int(input("What is the first number is the first number you would like to use:"))
                N2=int(input("What is the second number"))
                print("PRODUCT",N1*N2)
            if Operation=="/":
                N1=int(input("What is the first number is the first number you would like to use:"))
                N2=int(input("What is the second number"))
                if N1 == 0:
                    print("QUATION 0")
                elif N2 == 0:
                    print("QUATION 0")
                else :
                    if N1 < N2:
                        tab=N1
                        N1=N2
                        N2=tab
                    print("QUATION",N1/N2)
            if Operation=="%":
                N1=int(input("What is the first number is the first number you would like to use:"))
                N2=int(input("What is the second number"))
                tab=N1
                N1=N2
                N2=tab
                print("PERCENT",(N2/100)*N1)
            if Operation=="squared":
                N1=int(input("What is the first number is the first number you would like to use:"))
                print("SQUARD",N1*N1)
            if Operation=="square root":
                import math
                num=int(input("What is the number that you want to find the square root of?"))
                print("Square ROOT",math.sqrt(num))
            if Operation=="factors":
                N1=int(input("What is the first number is the first number you would like to use:"))
                i=2
                print("factors are")
                while i!=N1:
                    game=(N1%i)
                    if game==0:
                        print(i)
                    i=i+1
            if Operation=="peremeter":
                shape=input("What is the shape that you would like to find the pere meter of?(square,rectangle,circle,triangle)")
                if shape=="square":
                    side=int(input("What is one of the sides?"))
                    print("PERIMETER",side+side+side+side)
                if shape=="rectangle":
                    sidea=int(input("What is length?"))
                    sideb=int(input("What is breath?"))
                    print("PERIMETER",(sidea + sideb)*2)
                if shape=="triangle":
                    triside=int(input("What is length?"))
                    print("PERIMETER",triside*3)
                if shape=="circle":
                    import math
                    cirside=int(input("What is the radius of your circle?"))
                    print("Perimeter",(2*math.pi*cirside))
            if Operation=="area":
                shapen=input("What is the shape that you would like to find the area of?(square,rectangle,circle,triangle)")
                if shapen=="square":
                    squad=int(input("What is one of the sides?"))
                    print("AREA",side*side)
                if shapen=="rectangle":
                    side3=int(input("What is length?"))
                    side4=int(input("What is breath?"))
                    print("AREA",(side3+side4)*2)
                if shapen=="triangle":
                    side1=int(input("What is hight?"))
                    side2=int(input("What is breath?"))
                    area= 1/2*side1*side2
                    print("AREA",area)
                if shapen=="circle":
                    cirside=int(input("What is the radius of your circle?"))
                    print("AREA",(math.pi*cirside*cirside))
                else:
                    print("""You have not rendered something that this machine can do. You must have spelled it wrong, if you
                    want to try that again then please say yes.""")
            restart=input("Would you like to do that again? If you want to do that then type yes else type no.")
            if restart=="yes":
                rac()
        rac()

    if thing=="game":
        def boba():
            print("I have thought of a number that is in the range of 1-20")
            jeff=random.randint(1,21)
            # print(jeff)
            Turns=0
            while Turns != 6:
                guess=int(input("Please enter your guess?"))
                if guess==jeff:
                    print("You guessed it!!!")
                    break
                if guess!=jeff and guess<jeff:
                    print("You have guessed to low; please guess again.")
                    guess
                if guess!=jeff and guess>jeff:
                    print("You have guessed to high; please guess again.")
                    guess
            Turns=Turns+1
            restart1=input("Would you like to do that again? If you want to do that then type yes else type no.")
            if restart1=="yes":
                boba()
        boba()
bang()
restart=input("Would you like to do the other thing? If you want to then type yes else no.")
if restart=="yes":
    bang()

else:
    print("Goodbye")
