# f string is used to format strings
# ----------------- OLD Approach ----------------
letter = "Hello my name is {} and i am from {}"
country = "India"
name = "Nirdesh"
print(letter.format(name, country))
letter = "Hello my name is {1} and i am from {0}"
print(letter.format(country, name))

# ------------------- MODERN APPROACH ----------------
print(f"Hello my name is {name} and i am from {country}")  # This is called fstrings

price = 49.099999
txt = "For only {price: .2f} dollars"
print(txt.format(price=49.099999))
# OR with f string
txt = f"For only {price: .2f} dollars"
print(txt)

# we can find a string
print(f"{2 * 30}")

# if we want to print this as it is
print(f"Hello my name is {{name}} and i am from {{country}}")  # This is called fstrings
