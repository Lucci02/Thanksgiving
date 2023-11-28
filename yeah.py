cooking_time = 0
weight = 0

def calculate_cooking_time(weight):
    # Assuming 15 minutes per pound for cooking time
    cooking_time = weight * 15


print("Welcome to the Thanksgiving Turkey Cooking Time Calculator!")
# Get the weight of the turkey from the user
weight = str(input("Enter the weight of the turkey in pounds: "))
zero = float(weight)
time = float(weight) * 15
    # Validate that the weight is a positive number
while weight <= 0:
    print("Invalid input. Please enter a numerical weight above 0.")
    weight = float(input("Enter the weight of the turkey in pounds: "))
       
        
# Calculate the cooking time
cooking_time = calculate_cooking_time(weight)
        
# Display the cooking time
print("Estimated cooking time for a " + str(weight) + " pound turkey: " + str(time) + "minutes")


