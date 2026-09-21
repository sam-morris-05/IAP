# Prompt-and-Diff Log

## Prompt 1

### Prompt

What do I need to include in my repository for the first IAP milestone, and what
commands should I run to verify that Python, pip, pytest, and Git are working
correctly?

### Raw Output

The AI suggested creating a small project structure with a README, a basic
Python file, a simple pytest file, a prompt-and-diff log, and a .gitignore.

It also recommended using terminal commands such as:

- python --version
- pip --version
- pytest
- git --version
- git status

It also explained that the repository should be committed and pushed to GitHub
and that the final terminal evidence should show the runtime, test runner, and
Git repository status.

### What I Changed

I used the response as guidance while setting up the project environment.

I created the repository structure, wrote the README and concept brief, created
a basic Python file, added a simple test so pytest could run, and verified the
required tools from the VS Code terminal.

I also used the guidance to organize what evidence I needed to collect for the
milestone.

### Why the Original Was Wrong / Incomplete

Before using the AI guidance, I had not fully organized the repository or
verified all parts of the toolchain.

The AI helped me identify the required setup steps and organize the repository,
but I still had to create and verify the project on my computer.

## Prompt 2 - Requirements Elicitation

### Prompt

Elicit software requirements for a Python application called a Three-Phase
Power Calculator. The application is intended for electrical engineering users.
Provide user stories, acceptance criteria, and non-functional requirements.

### Raw Output

The AI suggested requirements involving three-phase calculations, Wye and
Delta systems, input validation, calculation history, file exporting, saved
settings, cross-platform support, and measurable calculation accuracy.

### What I Changed

I compared the generated requirements with the scope of the application I plan
to build.

I kept requirements that matched the project, revised requirements that needed
more detail, removed features that were outside my intended scope, and added
requirements the AI did not identify.

### Why the Original Was Wrong / Incomplete

The AI output was useful as a starting point, but it made assumptions about
features that were not part of my original concept.

It also did not ask enough questions about the exact scope before generating
the requirements, so the output required review before it accurately represented
the project.

## Prompt 3 — M3 Domain Model

### Prompt

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

### AI Output

The AI-generated domain model was saved in `M3_AI_DRAFT.md`.

The AI model included:

- `User`
- `UserSettings`
- `Calculation`
- `PowerCalculation`
- `CurrentCalculation`
- `VoltageCalculation`
- `PowerFactorCalculation`
- `WyeConnection`
- `DeltaConnection`
- `CalculationHistory`
- `ValidationService`
- `ExportService`
- `AuditLog`

### Changes I Made

I removed `User` and `UserSettings` because my M2 requirements do not include accounts, profiles, login features, or saved preferences.

I removed `CalculationHistory` because the application only needs to clear the current calculation. There is no requirement to save or display previous calculations.

I removed `ExportService` and `AuditLog` because exporting files and tracking user activity are outside the current scope of the application.

I removed the separate `PowerCalculation`, `CurrentCalculation`, `VoltageCalculation`, and `PowerFactorCalculation` subclasses. I decided that these calculations are related enough to be handled by one `CalculationService` instead of creating a separate class for every equation.

I replaced the separate `WyeConnection` and `DeltaConnection` classes with a `ConnectionType` enumeration containing `WYE` and `DELTA`.

I did not keep a separate `ValidationService`. Validation is closely related to whether a calculation request is valid, so I made it a responsibility of `CalculationService`.

I also split the AI's general `Calculation` class into:

- `CalculationRequest`
- `CalculationService`
- `CalculationResult`

This separates the values going into the calculation, the calculation logic itself, and the result returned by the calculator.

I added a `QuantityType` enumeration to represent the supported calculation choices:

- `POWER`
- `LINE_CURRENT`
- `LINE_VOLTAGE`
- `POWER_FACTOR`

### Why I Changed It

The AI draft included several features that are common in larger applications but are not required by my M2 requirements.

My final model is intentionally smaller. I wanted every major class or relationship to be tied directly to a requirement instead of adding features that the application may never need.

I also did not create classes for the non-functional requirements. Accuracy within 1%, passing all committed pytest tests, and returning a result within one second are constraints that should be checked through testing rather than represented as domain objects.

The final model therefore focuses on the main calculation flow:

`CalculationRequest -> CalculationService -> CalculationResult`

with `ConnectionType` and `QuantityType` used for the limited sets of valid choices.