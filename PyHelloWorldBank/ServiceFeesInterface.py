from abc import ABC, abstractmethod

class ServiceFeesInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def service_charge(self, amount: float) -> float:
        raise NotImplementedError
    