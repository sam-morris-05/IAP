# M3 Domain Model

```mermaid
classDiagram
direction LR

class CalculationRequest {
    +voltage: float
    +current: float
    +powerFactor: float
    +connectionType: ConnectionType
    +requestedQuantity: QuantityType
}

class CalculationService {
    +validate(request: CalculationRequest) bool
    +calculate(request: CalculationRequest) CalculationResult
    +clear()
}

class CalculationResult {
    +value: float
    +unit: string
    +quantity: QuantityType
}

class ConnectionType {
    <<enumeration>>
    WYE
    DELTA
}

class QuantityType {
    <<enumeration>>
    POWER
    LINE_CURRENT
    LINE_VOLTAGE
    POWER_FACTOR
}

CalculationRequest --> ConnectionType : uses
CalculationRequest --> QuantityType : requests
CalculationService --> CalculationRequest : receives
CalculationService --> CalculationResult : produces
CalculationResult --> QuantityType : identifies