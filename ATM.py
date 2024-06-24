class ATM:
    def __init__(self, initial_balance=2000):
        self.balance = initial_balance
        self.pin = "3399"

    def enter_pin(self):
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        else:
            self.balance -= amount
            print(f"Dispensing ${amount}")
            return True

    def display_balance(self):
        print(f"Your updated balance is: ${self.balance}")

    def run(self):
        if self.enter_pin():
            try:
                amount = float(input("Enter amount to withdraw: "))
                if self.withdraw(amount):
                    self.display_balance()
            except ValueError:
                print("Invalid amount entered. Please enter a numeric value.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
