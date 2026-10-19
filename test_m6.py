
"""M6 tests for the Three-Phase Power Calculator."""

import math
import pytest

from calculation_service import CalculationService
from models import CalculationRequest, ConnectionType
from storage import CalculationStorage


def make_request(voltage=480, current=10, pf=0.8,
                 connection=ConnectionType.WYE):
    return CalculationRequest(
        connection_type=connection,
        line_voltage=voltage,
        line_current=current,
        power_factor=pf,
    )


# Acceptance test: calculation through persistent storage
def test_m6_acceptance_calculation_and_storage(tmp_path):
    service = CalculationService()
    storage = CalculationStorage(tmp_path / "history.json")

    request = make_request()
    result = service.calculate(request)
    storage.save(result)

    saved = storage.load_latest()

    assert saved is not None
    assert saved["connection_type"] == "WYE"
    assert saved["line_voltage"] == 480
    assert saved["power_factor"] == 0.8
    assert saved["real_power"] == pytest.approx(
        6651.075102, rel=1e-6
    )
    assert saved["apparent_power"] == pytest.approx(
        8313.843876, rel=1e-6
    )
    assert len(storage.load_all()) == 1


# Unit test: real power at non-unity power factor
def test_real_power():
    result = CalculationService().calculate(make_request())

    assert result.real_power == pytest.approx(
        6651.075102, rel=1e-6
    )


# Unit test: zero power factor
def test_zero_power_factor():
    result = CalculationService().calculate(
        make_request(pf=0)
    )

    assert result.real_power == pytest.approx(0)
    assert result.reactive_power == pytest.approx(
        result.apparent_power
    )


# Unit test: unity power factor
def test_unity_power_factor():
    result = CalculationService().calculate(
        make_request(pf=1)
    )

    assert result.real_power == pytest.approx(
        result.apparent_power
    )
    assert result.reactive_power == pytest.approx(
        0, abs=1e-8
    )


# Unit test: Wye phase relationships
def test_wye_relationships():
    result = CalculationService().calculate(make_request())

    assert result.phase_voltage == pytest.approx(
        480 / math.sqrt(3)
    )
    assert result.phase_current == pytest.approx(10)


# Unit test: Delta phase relationships
def test_delta_relationships():
    result = CalculationService().calculate(
        make_request(connection=ConnectionType.DELTA)
    )

    assert result.phase_voltage == pytest.approx(480)
    assert result.phase_current == pytest.approx(
        10 / math.sqrt(3)
    )


# Unit tests: invalid inputs
@pytest.mark.parametrize(
    "voltage,current,pf",
    [
        (0, 10, 0.8),
        (-480, 10, 0.8),
        (480, -10, 0.8),
        (480, 10, -0.1),
        (480, 10, 1.1),
    ],
)
def test_invalid_inputs(voltage, current, pf):
    request = make_request(
        voltage=voltage,
        current=current,
        pf=pf,
    )

    with pytest.raises(ValueError):
        CalculationService().calculate(request)
