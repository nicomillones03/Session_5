name = input("What is your name? ")
print("Hello, ", name, "!", sep="")
age = input("How old are you? ")
try:
    age = int(age)  # convert string to integer
    birth_year = 2023 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("type a number to divide the age ")
    number = int(number)
    print(age/number)
except ValueError:
    print("Invalid age. Please enter numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except:
    print("Some other error I did not forsee.")
else:
    print("No exceptions were raised.")
finally:
    print("Thank you for playing.")
    