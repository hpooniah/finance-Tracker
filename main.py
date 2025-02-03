# Ask for monthly allowance and expenses in different categories

# Make a list
expanses = []

while True: 
    
    #Greet the user
    name =input("What is your name?").strip().lower()
    print(f"Hello{name}!\nThis is a Finace Tracker")

    invalid = True

    while invalid:
        try:
             # Ask user for how many different expanses
            num_expanses = int(input("How many expenses do you have? ").strip())
        except ValueError:
            print("Only type integers!")
        else: # When there is no error
            invalid = False
           
            # Loop as many items needed to add each item
            # Append each item to the list
    for i in range(num_expanses):
        try:
            expanse = int(float(input(f"Cost of each Expanse {i+1}: ")))
            expanses.append(expanse)
        except ValueError:
            print("Please enter a number for each expense")


            # Find total for expanses
            Total_expanses= sum(expanses)
            print(f"Your Total Expanses for this month are {round(Total_expanses,1)}")

            # Find the Monthly Allowance
            try:
                allowance = float(input("What's your monthly allowance? "))
            except ValueError:
                print("Please enter a number for your Monthly Allowance.")
                continue
                
            # Calculate how much left from allowance
            money_left = allowance - Total_expanses 
            print(f"You have {round(money_left, 2)} dolloars left from yout Monthly Allowence")

    # Ask user if they want to try again
    try_again = input("Do You Wish to find your monthly allowence agian? [y] or [n]").strip().lower()
    if try_again != "y":
        break

    print("Thank you for calculating with this student grade caculator program.")
    