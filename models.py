from dataclasses import dataclass
from enum import Enum


class ConnectionType(Enum):
    WYE = "WYE"
    DELTA = "DELTA"


@dataclass
class CalculationRequest:
    connection_type: ConnectionType
    line_voltage: float
    line_current: float
    power_factor: float


@dataclass
class CalculationResult:
    connection_type: str
    line_voltage: float
    line_current: float
    phase_voltage: float
    phase_current: float
    power_factor: float
    apparent_power: float
    real_power: float
    reactive_power: float