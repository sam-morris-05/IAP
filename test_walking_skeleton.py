import math

from calculation_service import CalculationService
from models import (
    CalculationRequest,
    ConnectionType,
)
from storage import CalculationStorage


def test_walking_skeleton_end_to_end(
    tmp_path,
):
    request = CalculationRequest(
        connection_type=ConnectionType.WYE,
        line_voltage=208.0,
        line_current=10.0,
        power_factor=0.85,
    )

    service = CalculationService()

    result = service.calculate(
        request
    )

    storage_file = (
        tmp_path / "calculations.json"
    )

    storage = CalculationStorage(
        storage_file
    )

    # Real file write.
    storage.save(
        result
    )

    # Real file read.
    saved_result = (
        storage.load_latest()
    )

    assert saved_result is not None

    assert (
        saved_result["connection_type"]
        == "WYE"
    )

    assert (
        saved_result["line_voltage"]
        == 208.0
    )

    assert (
        saved_result["line_current"]
        == 10.0
    )

    assert (
        saved_result["power_factor"]
        == 0.85
    )

    assert math.isclose(
        saved_result[
            "apparent_power"
        ],
        math.sqrt(3)
        * 208
        * 10,
        rel_tol=1e-6,
    )

    assert math.isclose(
        saved_result[
            "real_power"
        ],
        (
            math.sqrt(3)
            * 208
            * 10
            * 0.85
        ),
        rel_tol=1e-6,
    )