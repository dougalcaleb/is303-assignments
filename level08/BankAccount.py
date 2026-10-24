import random


class BankAccount:

    def __init__(self, user_name: str):
        self.balance = 0
        self.user_name = user_name
        self.account_number = random.randint(100000, 999999)

    def prompt_for_withdraw(self):
        print("How much would you like to withdraw?")
        chosen_amount = self._safe_float_prompt()
        self.withdraw(chosen_amount)
        print(f"Your balance is now ${self.balance:.2f}")
        print(" ")

    def prompt_for_deposit(self):
        print("How much would you like to deposit?")
        chosen_amount = self._safe_float_prompt()
        self.deposit(chosen_amount)
        print(f"Your balance is now ${self.balance:.2f}")
        print(" ")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Your balance is not enough for this withdrawal.")
            return

        self.balance -= amount

    def deposit(self, amount: float):
        self.balance += amount

    def view_info(self):
        print(f"Name: {self.user_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print(" ")

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