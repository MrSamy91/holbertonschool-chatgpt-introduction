class Checkbook:
    def __init__(self):
        """Initialize a new Checkbook instance."""
        self.balance = 0.0  # Initialize balance to zero

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to be deposited.

        """
        self.balance += amount  # Add the deposited amount to the balance
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to be withdrawn.

        """
        if amount <= 0:
            print("Invalid amount. Please enter a positive value for withdrawal.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Subtract the withdrawn amount from the balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.

    """
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        # Prompt the user for action (deposit, withdraw, balance, exit)
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
