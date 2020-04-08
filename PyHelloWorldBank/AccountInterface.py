from abc import ABC, abstractmethod

class AccountInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def deposit(self, amount: float) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def withdraw(self, amount: float) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_balance(self) -> float:
        raise NotImplementedError
