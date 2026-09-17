# AI Elicitation Audit

## Prompt Given to AI

Elicit software requirements for a Python application called a Three-Phase
Power Calculator. The application is intended for electrical engineering users.
Provide user stories, acceptance criteria, and non-functional requirements.


## AI-Generated Requirements

The AI suggested requirements involving:

- three-phase power calculations
- Wye and Delta support
- input validation
- calculation history
- CSV or PDF exporting
- remembering previous user settings
- Windows, macOS, and Linux support
- measurable calculation accuracy


## Audit

### What the AI Missed

The AI understood the general idea of the calculator, but it did not ask enough
questions about the exact scope.

It did not clearly determine which values should be solvable, such as line
voltage, line current, and power factor.

It also did not fully address blank or non-numeric input.

The main omission was that it started generating requirements before clarifying
the boundaries of the application.


### What the AI Invented

The AI introduced several requirements that were not part of my original
concept:

- calculation history
- CSV or PDF exporting
- saving user settings between sessions
- required Windows, macOS, and Linux compatibility

These could be useful features in a larger application, but they would expand
the project beyond the scope I intended.


### What the AI Got Right

The AI correctly identified three-phase electrical calculations, Wye and Delta
support, and input validation as important areas.

It also suggested making calculation accuracy measurable. This was useful
because it changed a vague goal such as "the calculator should be accurate"
into something that could actually be tested.

The AI also helped make the user stories and acceptance criteria more
consistent.


## Overall Judgment

The AI output was useful for reviewing and refining the requirements, but it
could not be accepted without review.

It identified several useful requirements, but it also missed scope details and
introduced features that I had not requested.

The final requirements therefore keep the useful parts of the AI output, remove
features that were outside the intended scope, and add requirements that better
match the Three-Phase Power Calculator I plan to build.