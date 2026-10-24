from BankAccount import BankAccount

print("Welcome to the bank!")
user_name = input("Please enter your name: ")

user_account = BankAccount(user_name)

bank_open = True

while bank_open:
    print("Please choose an option:")
    print(" ")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    print(" ")

    user_choice = -1

    while user_choice == -1:
        user_choice_input = input("")
        user_choice_input = user_choice_input.strip()

        if not user_choice_input in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        user_choice = int(user_choice_input)

        match user_choice:
            case 1:
                user_account.prompt_for_deposit()
            case 2:
                user_account.prompt_for_withdraw()
            case 3:
                user_account.view_info()
            case 4:
                bank_open = False
                print("Thank you for your business!")