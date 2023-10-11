def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    # Get weight and height input from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Display the result
    print("Your BMI is:", bmi)

if __name__ == "__main__":
    main()
