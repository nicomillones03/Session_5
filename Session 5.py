name = input("What is your name? ")
print("Hello, ", name, "!", sep="")
age = input("How old are you? ")
age = int(age)  # convert string to integer
birth_year = 2023 - age
print(name, ", you were born in ", birth_year, ".", sep="")
