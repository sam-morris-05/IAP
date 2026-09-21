# M3 AI Domain Model Critique

## Overview

The AI-generated domain model included several concepts that could make sense in a larger application, but I thought it added more structure than my current requirements justify. My final model is intentionally smaller because I wanted each class and relationship to have a clear reason for being there based on my M2 requirements.

## Over-Modelling

The biggest issue I found with the AI draft was over-modelling.

The AI added a `User` class along with a `UserSettings` class. My M2 requirements do not mention accounts, profiles, logging in, or saving user preferences. Because of that, I did not see a reason for either of these classes to exist in the current version of the application.

The AI also added a `CalculationHistory` class. My requirements allow the user to clear the calculator and begin another calculation, but they do not say that previous calculations need to be stored. I treated clearing the calculator as resetting the current inputs rather than maintaining a history of previous calculations.

The `ExportService` and `AuditLog` classes were also outside the scope of my requirements. There is no requirement to export results to CSV or PDF, and there is no requirement to keep a log of user activity.

Another example of over-modelling was the use of separate `PowerCalculation`, `CurrentCalculation`, `VoltageCalculation`, and `PowerFactorCalculation` subclasses. The application supports multiple calculations, but I did not think each equation needed its own class. At the current size of the project, one calculation service can choose the correct calculation based on what the user requests.

## Wye and Delta Representation

The AI created separate `WyeConnection` and `DeltaConnection` classes.

I decided to represent these differently. In my current requirements, Wye and Delta are choices that affect how a calculation is performed. They are not independent objects that need their own identity or stored state.

Because the application currently supports only those two connection types, I represented them using a `ConnectionType` enumeration containing `WYE` and `DELTA`.

If the application became more complex in the future and Wye and Delta required a large amount of separate behavior, using separate classes could make more sense. For the current project, I thought an enumeration was simpler and better matched the requirements.

## Validation

The AI created a separate `ValidationService`.

I agreed that validation is important, but I did not think it needed to be its own service for an application this small. I kept validation as a responsibility of the `CalculationService`.

This still allows the calculator to reject missing values, non-numeric inputs, negative values, invalid power factors, and other invalid inputs before performing a calculation.

## Input and Output Structure

The AI used one `Calculation` class to contain the inputs, calculation behavior, and final result.

I decided to separate these responsibilities.

My `CalculationRequest` represents the information going into a calculation. It contains values such as voltage, current, power factor, connection type, and the quantity that the user wants to calculate.

My `CalculationResult` represents the information coming back from the calculation. It contains the calculated value, its unit, and the type of quantity that was calculated.

This gives my model a simple flow:

`CalculationRequest -> CalculationService -> CalculationResult`

I thought this made each part of the model easier to understand and would also make the calculation logic easier to test.

## What the AI Got Right

The AI correctly identified voltage, current, power factor, and connection type as important parts of the calculator.

It also correctly recognized that the application needs to support power, current, voltage, and power-factor calculations.

The AI was also correct to include validation in the design. I disagreed with creating an entire separate service for it, but the behavior itself is required.

The AI also correctly recognized that Wye and Delta affect the calculations. My disagreement was mainly about how those choices should be represented in the model.

## Non-Functional Requirements

I did not create domain classes for the three non-functional requirements from M2.

The requirement that calculations be within 1% of the expected result is an accuracy constraint.

The requirement that all committed pytest tests pass is a verification constraint.

The requirement that a calculation return a result within one second is a performance constraint.

These requirements should be checked through testing instead of represented as domain entities. I did not think classes such as `Accuracy`, `Performance`, or `TestStatus` would represent actual objects in the calculator's domain.

## Final Design Choice

My final domain model uses three main classes:

- `CalculationRequest`
- `CalculationService`
- `CalculationResult`

It also uses `ConnectionType` and `QuantityType` enumerations for values that have a limited number of valid choices.

I chose this structure because it represents the actual flow of the application without adding features that are not currently required. The request contains the inputs, the service validates and performs the calculation, and the result contains the output.

The biggest difference between my model and the AI draft is that I treated my M2 requirements as the boundary of the current design. I did not include account management, saved preferences, calculation history, exporting, audit logging, or a large calculation class hierarchy because none of those features are necessary for the current project.