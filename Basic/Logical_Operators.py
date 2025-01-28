# has_good_credit=True
# has_high_income=False
# has_criminal_record=False

# if has_good_credit and not has_criminal_record:
#     print("Applicant is elegible")

#AND --Both shoulb be true
#OR  --Atleast one should be true
#Not --



#Comparision operator

# Name=input("Enter your Name:")

# if len(Name) < 3:
#     print("Must be atleast 3 characters")
# elif len(Name)>50:
#     print("Max is 50")
# else:
#     print("Nice name")


# project work
# Weight=int(input("Weight:"))
# unit=input("(L)for lbs or (K) for kg:")
# L=Weight*0.45
# K=Weight/0.45
# if unit == "L":
#     print(f"You are {L} kilos")
# else:
#     print(f"you are {K} Pounds")


 #while loop
# i=1
# while i<=5:
#     print('*' * i)
#     i=i+1
# print("Exited")

# Guessing Game

# secret_Number =9
# guess_Count=0
# guess_Limit=3

# while guess_Count < guess_Limit:
#     guess=int(input("Guess:"))
#     guess_Count+=1
#     if guess ==secret_Number:
#         print("YOU WON!")
#         break
# else:
#     print("You failed!")



#Car game
command=""
started=False
while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print("Car alreday started")
        else:
            started=True
            print("Car has started")
    elif command =="stop":
        if not started:
            print("Car already stopped")
        else:
            started=False
            print("Car has stopped")
    elif command =="help":
        print("""
start = to start the car
stop = to stop the car
quit=to quit the game""")
    elif command=="quit":
        break
    else:
        print("I dont understand that")

