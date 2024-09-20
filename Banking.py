
account_balance = 0.0
interest_rate = 0.05
def display_menu():
    print("select you operation:")
    print("Type D. For Deposit")
    print("Type W. For Withdraw")
    print("Type I. For Interest Calculation")
    print("Type B. For Show Balance")
    print("Type E. For Exiting the operation")
def deposit():
    global account_balance
    deposit_amount = float(input("Enter the deposit amount: "))
    account_balance += deposit_amount
def withdraw():
    global account_balance
    Withdraw_amount = float(input("Enter the withdraw amount: "))
    account_balance -= Withdraw_amount
def interest():
    global account_balance
    global interest_rate
    account_balance = account_balance + account_balance * interest_rate
def balance():
    global account_balance
    print(f"Your current balance is :$ {account_balance}")
def operator():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if(choice.upper() == 'D'):
            deposit()
        elif(choice.upper() == 'W'):
            withdraw()
        elif(choice.upper() == 'I'):
            interest()
        elif(choice.upper() == 'B'):
            balance()
        elif(choice.upper() == 'E'):
            print("Exiting..., Good bye!")
            break
        else: