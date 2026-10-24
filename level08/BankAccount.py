import random


class BankAccount:

    def __init__(self, user_name: str):
        self.balance = 0
        self.user_name = user_name
        self.account_number = random.randint(100000, 999999) # random 6-digit id for funsies

    # prompts the user for an amount to withdraw, then attempts a withdrawal.
    # withdrawal will fail if the current balance is lower than the requested amount.
    def prompt_for_withdraw(self):
        print("How much would you like to withdraw?")
        chosen_amount = self._safe_float_prompt()
        self.withdraw(chosen_amount)
        print(f"Your balance is now ${self.balance:.2f}")
        print(" ")

    # prompts the user for an amount to deposit, then performs the deposit
    def prompt_for_deposit(self):
        print("How much would you like to deposit?")
        chosen_amount = self._safe_float_prompt()
        self.deposit(chosen_amount)
        print(f"Your balance is now ${self.balance:.2f}")
        print(" ")

    # only handles actual withdrawals. guards against withdrawals exceeding the current balance
    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Your balance is not enough for this withdrawal.")
            return

        self.balance -= amount

    # only handles actual deposits
    def deposit(self, amount: float):
        self.balance += amount

    def view_info(self):
        print(f"Name: {self.user_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print(" ")

    # generic helper method to reduce duplication
    def _safe_float_prompt(self) -> float:
        user_input_valid = False
        chosen_value = 0

        while not user_input_valid:
            user_input = input("")

            try:
                chosen_value = float(user_input)
                user_input_valid = True
            except ValueError:
                print("Invalid value. Please enter a float.")

        return chosen_value