# JS, 1st, Financial Calculator
# ----- PSUEDOCODE -----
# Create savings function
# Create cic function
# ----- CODE -----
def savings():
    print("Welcome to the Savings Goal Calculator")
    goal = input("What amount are you saving to: ").strip().strip("$")
    while not isinstance(goal, int):
        goal = input("That was not a valid option. Please try again\n")
    time = input("How often are you contributing?\n 1. Weekly\n 2. Monthly\n 3. Semiyearly\n 4. Yearly\n").strip()
    while time != "1" and time != "2" and time != "3" and time != "4":
        time = input("That was not a valid option. Please try again\n")
    deposit = input("How much are you contributing each time: ").strip().strip("$")
    while not isinstance(deposit, int):
        deposit = input("That was not a valid option. Please try again\n")
    #CALCULATION HERE
    print(f"It will take result:.2f {"weeks" if time == "1" else "months" if time == "2" else "half-years" if time == "3" else "years"} to save ${goal}.")
def cic():
    print("Welcome to the Compound Interest Calculator")
    starting = input("Starting Amount: ").strip().strip("$")
    while not isinstance(starting, int):
        starting = input("That was not a valid option. Please try again\n")
    interest = input("Interest Rate Percent: ").strip().strip("%")
    while not isinstance(interest, int):
        interest = input("That was not a valid option. Please try again\n")
    years = input("Years Spent compounding: ").strip()
    while not isinstance(years, int):
        years = input("That was not a valid option. Please try again\n")
    def cycle():
        pass
        #CALCULATION
    for _ in range(years):
        cycle()
    print(f"At the end of {years} years you will have $result:.2f.")
def budget():
    print("Welcome to the Budget Allocator")
    num = input("How many budget categories do you have: ").strip().strip("$")
    while not isinstance(num, int):
        num = input("That was not a valid option. Please try again\n")
    for i in range(num):
        categories = []
        categories.append(input(f"Category {i}: ").strip())
    income = input("What is your monthly income: ").strip().strip("$")
    while not isinstance(income, int):
        income = input("That was not a valid option. Please try again\n")
    for category in categories:
        percent = input(f"What percent is {category}: ").strip().strip("%")
        while not isinstance(percent, int):
            percent = input("That was not a valid option. Please try again\n")
    for category in categories:
        result
        print(f"{category} is {}")
def sale_price():
    print("Welcome to the Sale Price Calculator")
def tip():
    print("Welcome to the Tip Calculator")

while True:
    print("\033c", end="")
    calc = input("Enter the number so select an option\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n 6. Exit\n")
    if calc == "6":
        print("Thank you for using this program.")
        break
    while calc != "1" and calc != "2" and calc != "3" and calc != "4" and calc != "5":
        calc = input("That was not a valid option. Please try again\n")
    print("\033c", end="")
    if calc == "1":
        savings()
    elif calc == "2":
        cic()
    elif calc == "3":
        budget()
    elif calc == "4":
        sale_price()
    else:
        tip()