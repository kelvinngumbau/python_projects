#nested if statements
number = float(input("Enter a number: "))
if number % 2 == 0:
    if number == 0:
        print("Number is even but zero")
    else:
        print("Number is even")
else:
    print("Number is Old")