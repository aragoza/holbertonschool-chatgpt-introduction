class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance.

    Attributes:
        balance (float): The current balance of the checkbook, initialized to 0.0.
    """

    def __init__(self):
        """Initialize a new Checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
            amount (float): The amount of money to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds exist.

        Parameters:
            amount (float): The amount of money to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook.

    Provides a simple command-line interface allowing the user to:
    - deposit money
    - withdraw money
    - check balance
    - exit the program
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()