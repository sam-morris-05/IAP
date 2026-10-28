
# M7 - Refactoring Note

**Project:** Three-Phase Power Calculator  
**Milestone:** M7 - Refactoring

## Code Smell Identified

The code smell I identified was a Long Method with
Multiple Responsibilities in calculation_service.py.

The calculate() method was responsible for validating
inputs, determining Wye and Delta phase relationships,
calculating power values, and returning the result.

Having all of this logic in one method made the code
harder to read and maintain.

## Refactoring Performed

I used the Extract Method technique to separate
the different responsibilities.

I created two helper methods:

- _validate_request() handles input validation.
- _calculate_phase_values() handles Wye and Delta
  phase voltage and current relationships.

The main calculate() method now calls these methods
and performs the power calculations.

I kept the original formulas, error messages,
and calculation outputs the same.

## What Became Easier

The code is now easier to understand because each
method has a specific responsibility.

If I need to change input validation or phase
calculations in the future, I can work on those
sections without changing the main calculation logic.

This also makes it easier to identify where a
problem might occur when debugging the application.

## Behavior Verification

I used the same pytest test suite before and after
refactoring.

No test files were modified during the refactor.

Before refactoring: 13 tests passed in 0.10 seconds.
After refactoring: 13 tests passed in 0.11 seconds.

