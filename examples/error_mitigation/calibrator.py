from functools import singledispatchmethod
from typing import Any 
from mitiq.typing import QuantumResult, QPROGRAM, MeasurementResult
import numpy as np


class BraketCalibrator:
    pass