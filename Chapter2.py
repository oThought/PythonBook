# Final Q

proverb = "A picture's worth a thousand words"
proverbImage = proverb.replace("A picture's", "An image is")
firstO = proverb.index("o")
proverbUpper = proverb.upper()
length = len(proverb)

print(proverb, proverbImage, firstO, proverbUpper, length)

def circle():
    radius = input("Radius = ")
    print(f"Area = {3.14159 * int(radius) ** 2}")
    print(f"Circumfrence = {3.14159 * 2 * int(radius)}")

circle()

def arithmatic():
    num1 = float(input("Num1 = "))
    num2 = float(input("Num2 = "))
    decimal = int(input("Decimal Point = "))
    print(f"The sum of {num1} and {num2} is {round(num1 + num2, decimal)}")
    print(f"The product of {num1} and {num2} is {round(num1 * num2, decimal)}")

arithmatic()