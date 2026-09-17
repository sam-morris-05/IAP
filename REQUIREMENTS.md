# Three-Phase Power Calculator Requirements

## User Stories

### User Story 1 - Calculate Three-Phase Power

As an electrical engineering user, I want to enter line voltage, line current,
and power factor so that I can calculate common three-phase power values.

#### Acceptance Criteria

- The user can enter line voltage in volts.
- The user can enter line current in amps.
- The user can enter a power factor between 0 and 1.
- The application calculates real power.
- The application calculates reactive power.
- The application calculates apparent power.
- Results are displayed with the appropriate engineering units.


### User Story 2 - Calculate Line Current

As an electrical engineering user, I want to calculate line current from known
power, voltage, and power factor values so that I can solve for an unknown
current.

#### Acceptance Criteria

- The user can select a line current calculation.
- The user can enter real power, line voltage, and power factor.
- The application displays the calculated current in amps.


### User Story 3 - Calculate Line Voltage

As an electrical engineering user, I want to calculate line voltage from known
power, current, and power factor values so that I can solve for an unknown
voltage.

#### Acceptance Criteria

- The user can select a line voltage calculation.
- The user can enter real power, line current, and power factor.
- The application displays the calculated voltage in volts.


### User Story 4 - Calculate Power Factor

As an electrical engineering user, I want to calculate power factor from real
and apparent power so that I can determine the system power factor.

#### Acceptance Criteria

- The user can enter real power.
- The user can enter apparent power.
- The application displays a power factor between 0 and 1.
- Real power greater than apparent power is rejected.


### User Story 5 - Select Wye or Delta

As an electrical engineering user, I want to select Wye or Delta so that the
calculator can use the correct line and phase relationships.

#### Acceptance Criteria

- Wye and Delta are available as options.
- The selected connection type is used when applying line and phase
  relationships.


### User Story 6 - Handle Invalid Input

As a user, I want invalid input to be rejected so that the application does not
produce misleading results.

#### Acceptance Criteria

- Invalid voltage values are rejected.
- Negative current values are rejected.
- Power factor values outside 0 to 1 are rejected.
- Blank required fields are rejected.
- Non-numeric values produce an error message.


### User Story 7 - Clear the Current Calculation

As a user, I want to clear my current inputs and results so that I can begin a
new calculation.

#### Acceptance Criteria

- The user can clear entered values.
- Previous results are removed.
- The application remains ready for another calculation.


## Non-Functional Requirements

### NFR 1 - Calculation Accuracy

For supported calculations and valid inputs, calculated values must be within
1% of the expected result from the corresponding standard three-phase equation.

### NFR 2 - Automated Test Reliability

Before a release is considered acceptable, 100% of the committed pytest tests
must pass.

### NFR 3 - Response Time

For valid input, the application must display the calculated result within
1 second on the development computer under normal operating conditions.