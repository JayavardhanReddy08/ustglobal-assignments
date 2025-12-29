#Write a Python program to handle a ZeroDivisionError.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("denominator zero is not allowed")
except ValueError:
    print("enter value")
else:
    print("Division successful.")

finally:
    print("Program execution completed.")
