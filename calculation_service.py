
import math

from models import (
    CalculationRequest,
    CalculationResult,
    ConnectionType,
)


class CalculationService:
    def _validate_request(
        self,
        request: CalculationRequest,
    ) -> None:
        """Validate the inputs for a calculation."""
        if request.line_voltage <= 0:
            raise ValueError(
                "Line voltage must be greater than zero."
            )

        if request.line_current < 0:
            raise ValueError(
                "Line current cannot be negative."
            )

        if not 0 <= request.power_factor <= 1:
            raise ValueError(
                "Power factor must be between 0 and 1."
            )

    def _calculate_phase_values(
        self,
        request: CalculationRequest,
    ) -> tuple[float, float]:
        """Calculate phase voltage and current."""
        if request.connection_type == ConnectionType.WYE:
            phase_voltage = (
                request.line_voltage / math.sqrt(3)
            )
            phase_current = request.line_current

        elif request.connection_type == ConnectionType.DELTA:
            phase_voltage = request.line_voltage
            phase_current = (
                request.line_current / math.sqrt(3)
            )

        else:
            raise ValueError(
                "Unsupported connection type."
            )

        return phase_voltage, phase_current

    def calculate(
        self,
        request: CalculationRequest,
    ) -> CalculationResult:
        """Perform the three-phase power calculation."""
        self._validate_request(request)

        phase_voltage, phase_current = (
            self._calculate_phase_values(request)
        )

        apparent_power = (
            math.sqrt(3)
            * request.line_voltage
            * request.line_current
        )

        real_power = (
            apparent_power
            * request.power_factor
        )

        reactive_power = math.sqrt(
            max(
                0,
                apparent_power**2
                - real_power**2,
            )
        )

        return CalculationResult(
            connection_type=request.connection_type.value,
            line_voltage=request.line_voltage,
            line_current=request.line_current,
            phase_voltage=phase_voltage,
            phase_current=phase_current,
            power_factor=request.power_factor,
            apparent_power=apparent_power,
            real_power=real_power,
            reactive_power=reactive_power,
        )
