print("Welcome to the vehicle picker")
print("What type of vehicle would you like?")
print("1. Car")
print("2.Bike")
print()

a=int(input("Enter 1 or 2"))

if a==1:
    print("What type of car would you like?")
    print("1.Volkswagen Beetle")
    print("2.Porsche 911")
    print()
    b=int(input("Enter 1 or 2"))

    if b==1:
        print("You now own a Volkswagen Beetle.\n its top speed is around 62 MPH and you have 4 seats")

    if b==2:
            print("You now own a Porsche 911.\n its top speed is around 183 MPH and you have 4 seats")

if a==2:
    print("What type of car would you like?")
    print("1.Cruiser")
    print("2.Underbone")
    print()
    c=int(input("Enter 1 or 2"))

    if c==1:
            print("You now own a Cruiser.\n its top speed is around 170 MPH and you have 1 seat")
    
    if c==2:
            print("You now own a Underbone.\n its top speed is around 50 MPH and you have 1 seat")