# Ask for monthly allowance and expenses in different categories

# Make a list
allowance_list = []

while True: 
    
    #Greet the user
    name =input("What is your name?").strip().lower()
    print(f"Hello{name}!\nThis is a monthly allowance calculator")

    invalid = True

    while invalid:
        try:
             # Ask user for how many different expanses
            num_allowance = int(input("How many assignemnets do you want to have averaged? ").strip())
        except ValueError:
            print("Only type integers!")
        else: # When there is no error
            invalid = False
           
            # Loop as many items needed to add each item
            # Append each item to the list
            for i in range(num_allowance):
                grade = int(float(input(f"Grade for the assignment {i+1}: ")))
                allowance_list.append(grade)

            # Find average for the assignment grades
            grades_sum = sum(allowance_list)
            average_grade = grades_sum / num_allowance

            print(f"Your average grade is {round(average_grade,1)}")


    # Ask user if they want to play again
    play_again = input("Do You Wish To Calculate Agian? [y] or [n]").strip().lower()
    if play_again != "y":
        break

    print("Thank you for calculating with this student grade caculator program.")




# Calculate total expenses and remaining balance
# Display results
# Conditional message based on balance (depending on whether you overspent or underspent or spent just the right amount, write a specific message - try to be kind!)


