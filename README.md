# Three-Phase Power Calculator

## Concept Brief

For my IAP project, I plan to build a three-phase power calculator using Python.
The program will allow a user to enter values such as voltage, current, and
power factor and calculate common three-phase power quantities.

As the project develops, I plan to add calculations for real power, reactive
power, and apparent power while keeping the program simple and easy to test.

## Declared Stack

- Python
- Visual Studio Code
- pip
- pytest
- Git
- GitHub
- GitHub Copilot
- ChatGPT

## Three-Phase Power Calculator

The application is a Python desktop calculator for common balanced
three-phase electrical calculations.

The application currently supports:

- Three-phase real, reactive, and apparent power
- Wye and Delta line/phase relationships
- Line current calculation
- Line voltage calculation
- Power factor calculation
- Input validation
- Calculation history using JSON storage
- Clearing the current calculation

## Setup

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```
## M5 Walking Skeleton

The M5 walking skeleton implements one complete three-phase power calculation
path through the application.

The user enters line voltage, line current, power factor, and Wye or Delta
connection type through the graphical interface. The request is passed to the
calculation service, the calculated result is written to JSON storage, the
stored result is read back, and that persisted result is displayed in the GUI.

## Setup

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

## Running the Tests

```bash
python -m pytest -v
```


---

## M6 – Testing and Bug Injection

Milestone 6 introduces additional automated testing and demonstrates the ability of the test suite to detect realistic calculation faults.

### Automated Testing

The project uses pytest to test:

- Three-phase real power calculations
- Zero and unity power factor
- Wye and Delta connection relationships
- Invalid input handling
- Calculation and JSON storage integration

Run the complete test suite:

    python -m pytest -v

### Code Coverage

Generate a coverage report using:

    python -m pytest --cov=calculation_service --cov=storage --cov-report=term-missing --cov-report=html

M6 baseline coverage: 95%

### Bug Injection Demonstration

A temporary calculation error was introduced by replacing the user's power factor with a constant value of 1.0.

This produced incorrect real-power results and caused four automated tests to fail.

The correct calculation was subsequently restored.

### Testing Documentation

See M6_TESTING_EVIDENCE.md for the testing summary.

See the m6_evidence folder for:

- Initial passing test output
- Coverage report
- Injected fault diff
- Failing test output
- Fix evidence
- Final passing test output
