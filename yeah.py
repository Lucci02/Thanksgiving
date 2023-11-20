def calculate_cooking_time(weight):
    # Assuming 15 minutes per pound for cooking time (you can adjust this as needed)
    cooking_time = weight * 15
    return cooking_time

def main():
    print("Welcome to the Thanksgiving Turkey Cooking Time Calculator!")
    
    try:
        # Get the weight of the turkey from the user
        weight = float(input("Enter the weight of the turkey in pounds: "))
        
        # Validate that the weight is a positive number
        if weight <= 0:
            print("Invalid input. Please enter a positive weight.")
            return
        
        # Calculate the cooking time
        cooking_time = calculate_cooking_time(weight)
        
        # Display the cooking time
        print(f"\nEstimated cooking time for a {weight} pound turkey: {cooking_time} minutes")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the weight.")

if __name__ == "__main__":
    main()
