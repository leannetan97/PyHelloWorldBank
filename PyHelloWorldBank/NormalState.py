from State import *
from Account import *

class NormalState(State):
    
    def __init__(self, account: Account):
        self._account = account
        (self._account).set_up_normal_state(self)
    
    # Override
    def get_state_name(self) -> str:
        return 'Normal State'
    
    # Override
    def withdraw(self, amount: float) -> str:
        charges = (self._account).get_service_charge(amount)
        total = charges + amount
        
        if (amount >= 1000 and total <= (self._account).get_balance()):
            (self._account).decrease_balance(total)
            self.__update_state()
            return 'RM' + str(amount) + ' with additional charges RM' + str(charges) + ' is deduct from the account\nCurrent Account State:' + (self._account).current_state.get_state_name() + '\nAccount Balance: RM' + str((self._account).get_balance()) + '\n';
        elif (amount < 1000 and amount <= (self._account).get_balance()):
            (self._account).decrease_balance(amount)
            self.__update_state()
            return 'RM' + str(amount) +' is deduct from the account\nCurrent Account State: ' + (self._account).current_state.get_state_name() + '\nAccount Balance: RM' + str((self._account).get_balance()) + '\n'
        else:
            return 'Sorry, Withdraw amount is more than account balance.\nWithdraw transaction is denied.\n'
        
    # Override
    def deposit(self, amount: float) -> str:
        (self._account).increase_balance(amount)
        return 'RM' + str(amount) + ' is added to the account\nCurrent Account State: ' + (self._account).current_state.get_state_name() + '\nAccount Balance: RM' + str((self._account).get_balance()) + '\n';
    
    def __update_state(self) -> None:
        if((self._account).get_balance() < 50):
            (self._account).set_state((self._account).lock_state)