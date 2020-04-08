from ServiceFeesInterface import *

class ServiceFees(ServiceFeesInterface):
    
    def __init__(self):
        pass
    
    # Override
    def service_charge(self, amount: float) -> float:
        return amount* 0.01