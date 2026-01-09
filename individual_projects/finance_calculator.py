# JS, 1st, Financial Calculator
# ----- PSUEDOCODE -----
# Create savings function
# Create cic function
# ----- CODE -----
def savings():
    print("Welcome to the Savings Goal Calculator")
    goal = input("What amount are you saving to: ").strip().strip("$")
    while True:
        try:
            goal = int(goal)
            break
        except:
            goal = input("That was not a valid option. Please try again\n").strip().strip("$")
    time = input("How often are you contributing?\n 1. Weekly\n 2. Monthly\n 3. Semiyearly\n 4. Yearly\n").strip()
    while time != "1" and time != "2" and time != "3" and time != "4":
        time = input("That was not a valid option. Please try again\n")
    deposit = input("How much are you contributing each time: ").strip().strip("$")
    while True:
        try:
            deposit = int(deposit)
            break
        except:
            deposit = input("That was not a valid option. Please try again\n").strip().strip("$")
    print("\033c", end="")
    result = 0
    count = 0 
    while count < goal:
        count += deposit
        result += 1 
    print(f"It will take {result:.2f} {"weeks" if time == "1" else "months" if time == "2" else "half-years" if time == "3" else "years"} to save ${goal}.")
def cic():
    print("Welcome to the Compound Interest Calculator")
    starting = input("Starting Amount: ").strip().strip("$")
    while True:
        try:
            starting = int(starting)
            break
        except:
            starting = input("That was not a valid option. Please try again\n").strip().strip("$")
    interest = input("Interest Rate Percent: ").strip().strip("%")
    while True:
        try:
            interest = int(interest)
            break
        except:
            interest = input("That was not a valid option. Please try again\n").strip().strip("$")
    years = input("Years Spent compounding: ").strip()
    while True:
        try:
            years = int(years)
            break
        except:
            years = input("That was not a valid option. Please try again\n").strip()
    def cycle():
        pass
        #CALCULATION
    for _ in range(years):
        cycle()
    print("\033c", end="")
    print(f"At the end of {years} years you will have $result:.2f.")
def budget():
    print("Welcome to the Budget Allocator")
    num = input("How many budget categories do you have: ").strip()
    while True:
        try:
            num = int(num)
            break
        except:
            num = input("That was not a valid option. Please try again\n").strip()
    for i in range(num):
        categories = []
        categories.append(input(f"Category {i}: ").strip())
    income = input("What is your monthly income: ").strip().strip("$")
    while not isinstance(income, int):
        income = input("That was not a valid option. Please try again\n")
    for category in categories:
        percentages = []
        percent = input(f"What percent is {category}: ").strip().strip("%")
        while True:
            try:
                percent = int(percent)
                break
            except:
                percent = input("That was not a valid option. Please try again\n").strip().strip("%")
        percentages.append(percent)
    print("\033c", end="")
    for i in range(num):
        result = income*percentages[i]
        print(f"{category} is {result}", end=", ")
def sale_price():
    print("Welcome to the Sale Price Calculator")
    cost = input("How much does the item originally cost: ").strip().strip("$")
    while True:
        try:
            cost = int(cost)
            break
        except:
            cost = input("That was not a valid option. Please try again\n").strip().strip("$")
    discount = input("What percent is the discount: ").strip().strip("%")
    while True:
        try:
            discount = int(discount)
            break
        except:
            discount = input("That was not a valid option. Please try again\n").strip().strip("%")
    print("\033c", end="")
    result = cost - (cost * (discount / 100))
    print(f"The item now costs ${result}")
def tip():
    print("Welcome to the Tip Calculator")
    bill = input("How much is the bill: ").strip().strip("$")
    while True:
        try:
            bill = int(bill)
            break
        except:
            bill = input("That was not a valid option. Please try again\n").strip().strip("$")
    tip = input("What percent of a tip are you giving: ").strip().strip("%")
    while True:
        try:
            tip = int(tip)
            break
        except:
            tip = input("That was not a valid option. Please try again\n").strip().strip("%")
    print("\033c", end="")
    result = bill + (bill * (tip / 100))
    print(f"The item now costs ${result}")

print("\033c", end="")
while True:
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