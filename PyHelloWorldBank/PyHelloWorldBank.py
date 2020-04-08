# Method 1
from ServiceFees import *
from LockState import *
from NormalState import *
from Account import *

# Method 2
# import ServiceFees as sf
# import Account as acc
# import LockState as lock
# import NormalState as normal
# >> sf.ServiceFees()
# >> lock.LockState()

# Method 3
# import ServiceFees
# import Account
# import LockState
# import NormalState
# >> ServiceFees.ServiceFees()
# >> LockState.LockState()

def inputValidation(amount: str) -> float:
    try :
        return float(amount);
    except ValueError :
        return -1;

def optionValidation(option: str) -> int:
    try :
        return int(option);
    except Exception as e :
        return 5;

def main():
    print('Hello World Bank')

    account = Account(ServiceFees())
    LockState(account)
    NormalState(account)

    print('Welcome to Hello World Bank :)')

    while(True):
        option = optionValidation(input('1. Deposit\n2. Withdraw\n3. View Balance\n4. Exit\nChoose Option (1 - 4):'))

        if(option == 1):
            amount = inputValidation(input("Please enter deposit amount:"))

            while(amount < 1):
                if amount == 0:
                    amount = inputValidation(input('Deposit amount cannot be 0 or less than 0. Please enter the deposit amount: '))
                else:
                    amount = inputValidation(input('Invalid amount. Please enter the deposit amount: '))

            print(account.deposit(amount))

        elif(option == 2):
            amount = inputValidation(input('Please enter withdrawal amount:\n(Note: 1% of addition service charge will be charged if the withdrawal amount more than or equal to RM1000)\n'))
            while(amount < 1):
                if amount == 0:
                    amount = inputValidation(input('Withdraw amount cannot be 0 or less than 0. Please enter the withdraw amount: '))
                else:
                    amount = inputValidation(input('Invalid amount. Please enter the withdraw amount: '))
            print(account.withdraw(amount))
            
        elif(option == 3):
            print('Account Balance: RM', str(account.get_balance()), '\n')

        elif(option == 4):
            print('Thank you for choosing Hello World Bank. Have a nice day! Thank you. :)\n')
            break

        else:
            print('Opps,Invalid option. Please choose again.')

if __name__ == "__main__": 
    main()