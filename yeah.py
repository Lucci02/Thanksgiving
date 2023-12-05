weight = 0
cooking_time = weight * 15
#intro
print("Welcome to the Thanksgiving Turkey Cooking Time Calculator!")
#determine input validity
while True:
    weight_input = input("Enter the weight of the turkey in pounds: ")
#Looked up how to do this (if you remember will you explain it to me in class?)
    if weight_input.replace(".", "", 1).isdigit():
        weight = float(weight_input)
        break
    else:
        print("Invalid input. Please enter a numeric value for the weight.")
#calculate
cooking_time = weight * 15
#print out value
print("For a " + str(weight) + "-pound turkey, the estimated cooking time is " + str(cooking_time) + " minutes.")
