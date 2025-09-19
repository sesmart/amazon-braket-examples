from functools import singledispatchmethod
from typing import Any 
from mitiq.typing import QuantumResult, QPROGRAM, MeasurementResult
import numpy as np
from braket.circuits import Circuit

class BraketExecutor:
    def __init__(self, result = None):
        pass

    @singledispatchmethod
    def execute(self, arg : Any):
        raise TypeError
    
    def __call__(self, *args, **kwargs):
        return self.execute(*args, **kwargs)
    
    @execute.register(list)
    def execute(self, circ : list[Circuit]):
        pass

    @execute.register(Circuit)
    def execute(self, circ : Circuit):
        pass
