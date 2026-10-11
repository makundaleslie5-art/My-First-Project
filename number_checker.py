try:
    number = float(input("Enter any number: "))

    if number > 0:
        print("Your number is positive.")
    elif number < 0:
        print("Your number is negative.")
    else:
        print("Your number is zero.")

except ValueError:
    print("Invalid input! Please enter a number.")
