weight = 0


print("Hey! Welcome to the Turkey Cooking Time Calculator!")


while True:
    weight_input = input("How heavy is your turkey is in pounds: ")


    if weight_input.isdigit():
        weight = float(weight_input)
        break
    else:
        print("Oops! That doesn't look like a number. Please enter the weight as a number.")


cooking_time = weight * 15


print("For a " + str(weight) + "-pound turkey, it should take about " + str(cooking_time) + " minutes to cook.")


