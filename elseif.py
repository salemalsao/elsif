
gender = input("What is your gender (male or female): ")
hight = input("Are you tall? ")


if gender == "male" and hight == "yes":
    print("You are a tall male")
elif gender == "male" and hight == "no":
    print("You are a short male")
elif gender == "female" and hight == "yes":
    print("You are a tall female")
elif gender == "female" and hight == "no":
    print("You are a short female")
else:
    print("Your input is invalid, try again")


