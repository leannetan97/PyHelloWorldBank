from State import *
from Account import *

class LockState(State):
    
    def __init__(self, account: Account):
        self._account = account
        (self._account).set_up_lock_state(self)
    
    # Override
    def get_state_name(self) -> str:
        return 'Lock State'
    
    # Override
    def withdraw(self, amount: float) -> str:
        return 'Sorry, Unable to perform withdrawal. Account should have minimum RM50 in order to perform withdrawal.\nCurrent Account State: ' + (self._account).current_state.get_state_name()  + '\nAccount Balance: RM' + str((self._account).get_balance()) + '\n'
        
    # Override
    def deposit(self, amount: float) -> str:
        (self._account).increase_balance(amount)
        self.__update_state()
        return 'RM' + str(amount) + ' is added to the account\nCurrent Account State: ' + ((self._account).current_state).get_state_name() + '\nAccount Balance: RM' + str((self._account).get_balance()) + '\n'
    
    def __update_state(self) -> None:
        if((self._account).get_balance() >= 50):
            (self._account).set_state((self._account).normal_state)