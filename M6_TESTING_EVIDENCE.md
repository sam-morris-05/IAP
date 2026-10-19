
# M6 – Testing and Bug Injection Evidence

## Project
Three-Phase Power Calculator

## 1. Acceptance Testing

An acceptance test was developed to verify the complete M5 walking skeleton.

The test creates a calculation request, processes it through CalculationService, saves the result using CalculationStorage, and reads the result from a JSON file.

The test verifies that the stored values match the expected electrical calculations.

Both the original M5 walking skeleton test and the new M6 acceptance test passed before fault injection.

## 2. Unit Testing

Unit tests were added to verify the following behaviors:

- Real power calculation
- Zero power factor
- Unity power factor
- Wye phase voltage and current relationships
- Delta phase voltage and current relationships
- Invalid voltage inputs
- Invalid current inputs
- Invalid power factor inputs

The existing tests were retained to ensure compatibility with previous milestones.

## 3. Initial Test Results

Command:
python -m pytest -v

Results:
- 13 tests passed
- 0 tests failed
- Execution time: 0.07 seconds

Evidence:
m6_evidence/tests_pass_before.txt

## 4. Code Coverage

Command:
python -m pytest --cov=calculation_service --cov=storage --cov-report=term-missing --cov-report=html

Coverage Results:

| File | Statements | Missed | Coverage |
|---|---:|---:|---:|
| calculation_service.py | 21 | 1 | 95% |
| storage.py | 22 | 1 | 95% |
| Total | 43 | 2 | 95% |

The coverage report demonstrates that the automated tests exercise 95% of the measured calculation and storage code.

Evidence:
m6_evidence/coverage_report.txt

HTML Coverage Report:
htmlcov/index.html

## 5. Bug Injection

A deliberate fault was introduced into calculation_service.py.

Original calculation:

    real_power = apparent_power * request.power_factor

Injected fault:

    real_power = apparent_power * 1.0

This fault causes the calculator to ignore the user's entered power factor and incorrectly assume unity power factor.

For a system with:
- Line voltage: 480 V
- Line current: 10 A
- Power factor: 0.8

Expected real power: 6651.08 W

Faulty real power: 8313.84 W

This is a realistic engineering error because the calculated power remains a plausible numerical value but is physically incorrect for the given power factor.

Evidence:
m6_evidence/fault_diff.txt

## 6. Fault Injection Test Results

After introducing the fault, the automated test suite was executed again.

Results:
- 9 tests passed
- 4 tests failed
- Execution time: 0.20 seconds

Failed Tests:

1. test_m6_acceptance_calculation_and_storage
2. test_real_power
3. test_zero_power_factor
4. test_walking_skeleton_end_to_end

The failures demonstrate that the test suite detects an incorrect real-power calculation.

The original M5 walking skeleton test also detected the fault, demonstrating that previously developed acceptance testing remains effective.

Evidence:
m6_evidence/tests_fail_injected.txt

## 7. Fault Correction

The injected fault was removed by restoring the original calculation:

    real_power = apparent_power * request.power_factor

The test suite was then rerun to verify that the application returned to its correct behavior.

Final test results:
[Enter actual final passing test count]

Evidence:
m6_evidence/tests_pass_after.txt
m6_evidence/fix_evidence.txt

## 8. Conclusion

The M6 testing process demonstrated that the Three-Phase Power Calculator's automated tests detect realistic calculation errors.

The initial test suite passed all 13 tests and achieved 95% coverage across the calculation and storage modules.

A deliberate power factor calculation fault caused four tests to fail, demonstrating that the tests verify meaningful engineering behavior rather than simply checking whether the program executes.

The original calculation was restored and the suite was rerun to confirm correct operation.
