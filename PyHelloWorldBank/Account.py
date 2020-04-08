from ServiceFeesInterface import *
from State import *
from AccountInterface import *

class Account(AccountInterface):
    
    def __init__(self, service_fees: ServiceFeesInterface):
        # Instance Variable
        self._service_fees = service_fees
        self._lock_state = None
        self._normal_state = None
        self._current_state = None
        self._balance = 0
    
    # Override
    def deposit(self, amount: float) -> str:
        print('=== DEPOSIT ===')
        return (self._current_state).deposit(amount)
    
    # Override
    def withdraw(self, amount: float) -> str:
        print('=== WITHDRAW ===')
        return (self._current_state).withdraw(amount)
    
    # Override
    def get_balance(self) -> float:
        return round(self._balance, 2)
    
    def set_state(self, state: State) -> None:
        self._current_state = state
    
    def set_up_normal_state(self, normal_state: State) -> State:
        self._normal_state = normal_state
        
    def set_up_lock_state(self, lock_state: State) -> State:
        self._lock_state = lock_state
        self._current_state = self._lock_state
    
    # @Proprety is to access getter, method to call self.normal_state
    @property
    def normal_state(self) -> State:
        return self._normal_state
    
    @property
    def lock_state(self) -> State:
        return self._lock_state
    
    @property
    def current_state(self) -> State:
        return self._current_state
      
    def get_service_charge(self, amount: float) -> float:
        return (self._service_fees).service_charge(amount)
    
    def increase_balance(self, amount: float) -> None:
        self._balance += amount
        
    def decrease_balance(self, amount: float) -> None:
        self._balance -= amount