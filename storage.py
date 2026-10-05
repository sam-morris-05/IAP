import json
from dataclasses import asdict
from pathlib import Path

from models import CalculationResult


class CalculationStorage:
    def __init__(
        self,
        filename="calculations.json",
    ):
        self.filename = Path(filename)

    def load_all(self):
        if not self.filename.exists():
            return []

        with open(
            self.filename,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def save(
        self,
        result: CalculationResult,
    ):
        calculations = self.load_all()

        calculations.append(
            asdict(result)
        )

        with open(
            self.filename,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                calculations,
                file,
                indent=4,
            )

    def load_latest(self):
        calculations = self.load_all()

        if not calculations:
            return None

        return calculations[-1]