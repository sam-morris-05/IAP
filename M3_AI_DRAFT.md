# M3 AI Domain Model Draft

## Prompt Given to AI

Using the following M2 requirements for my Three-Phase Power Calculator, create a domain model as a Mermaid class diagram.

The application requirements include:

- Calculate three-phase power from electrical inputs.
- Calculate line current when the required values are provided.
- Calculate line voltage when the required values are provided.
- Calculate power factor when the required values are provided.
- Support both Wye and Delta connections.
- Validate missing, non-numeric, or invalid input before performing a calculation.
- Allow the user to clear the calculator and enter a new calculation.
- Calculations must be within 1% of the expected result.
- All committed pytest tests must pass.
- A calculation must return a result within 1 second.

Identify the important domain classes, attributes, methods, and relationships.

## AI-Generated First Draft

```mermaid
classDiagram
direction LR

class User {
    +userId: int
    +name: string
    +email: string
    +createCalculation()
    +viewHistory()
}

class UserSettings {
    +defaultConnectionType: string
    +preferredVoltageUnit: string
    +preferredCurrentUnit: string
    +savePreferences()
}

class Calculation {
    +calculationId: int
    +voltage: float
    +current: float
    +powerFactor: float
    +connectionType: string
    +result: float
    +timestamp: datetime
    +validateInputs()
    +calculate()
    +clear()
}

class PowerCalculation {
    +calculatePower()
}

class CurrentCalculation {
    +calculateCurrent()
}

class VoltageCalculation {
    +calculateVoltage()
}

class PowerFactorCalculation {
    +calculatePowerFactor()
}

class WyeConnection {
    +convertLineToPhase()
    +convertPhaseToLine()
}

class DeltaConnection {
    +convertLineToPhase()
    +convertPhaseToLine()
}

class CalculationHistory {
    +historyId: int
    +calculations: List
    +addCalculation()
    +deleteCalculation()
    +clearHistory()
}

class ValidationService {
    +validateNumericInput()
    +validatePowerFactor()
    +validatePositiveValues()
}

class ExportService {
    +exportCSV()
    +exportPDF()
}

class AuditLog {
    +logId: int
    +timestamp: datetime
    +action: string
    +recordAction()
}

User "1" --> "1" UserSettings : has
User "1" --> "1" CalculationHistory : owns
CalculationHistory "1" --> "*" Calculation : stores

Calculation <|-- PowerCalculation
Calculation <|-- CurrentCalculation
Calculation <|-- VoltageCalculation
Calculation <|-- PowerFactorCalculation

Calculation --> WyeConnection : may use
Calculation --> DeltaConnection : may use
Calculation --> ValidationService : validates with
Calculation --> ExportService : exports through
Calculation --> AuditLog : records