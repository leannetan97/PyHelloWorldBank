from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def get_state_name(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def withdraw(self, amount: float) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def deposit(self, amount: float) -> str:
        raise NotImplementedError